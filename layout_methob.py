from typing import Union, Literal, Optional, Any

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QPushButton, QTabWidget


def layout_setting(layout: Union[QVBoxLayout, QHBoxLayout, QGridLayout], *widgets) -> None:
    """
    add widgets to layout
    """
    # self.setLayout(layout)

    for makes in range(len(widgets)):
        layout.addWidget(widgets[makes])


def general_layout(widgets: Union[tuple[Any], list[Any]], self: QWidget,
                   layout: Union[Any],
                   ):
    layout_setting(layout, *widgets)
    self.setLayout(layout)


def layout_modes(widgets: tuple | list, self: QWidget,
                 layout: Union[Any],
                 mode: Literal[
                     'vbox', 'vbox_top', 'vbox_down', 'vbox_center', 'vbox_factor', 'vbox_customer_distance', 'vbox_space',
                     'hbox', 'hbox_left', 'hbox_right', 'hbox_center', 'hbox_customer_distance', 'hbox_space', 'hbox_margins', 'grid', 'vbox_margins', 'form'] = 'vbox'
                 , item_location: int = 0, item_distance: Optional[Union[int, list[int], tuple[int], None]] = None,
                 space_distance: int = 10,
                 margins: Optional[Union[tuple, None]] = None,
                 alignment: Union[list[Qt.AlignmentFlag], tuple[Qt.AlignmentFlag], None] = None,
                 widget_position: Union[tuple, None] = None, element_name: Union[list, tuple, None] = None
                 ):
    total_index = len(widgets)
    if item_distance is None:
        lad_list = [i for i in range(total_index)]
        item_distance = round(sum(lad_list) / len(lad_list))
    if alignment is None:
        alignment = [Qt.AlignmentFlag(0) for _ in range(total_index)]
    if element_name is None:
        element_name = ['' for _ in range(total_index)]

    match mode:

        case 'vbox':
            assert (isinstance(layout, QVBoxLayout)), "layout type is QVboxLayout"
            general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_down':
            if not isinstance(layout, (QGridLayout, QFormLayout)):
                layout.addStretch()
            general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_top':
            assert (isinstance(layout, QVBoxLayout)), "layout type is QVboxLayout"
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.addStretch()
        case 'hbox_left':
            if not isinstance(layout, (QGridLayout, QFormLayout)):
                layout.addStretch()
            general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_center':
            layout.addStretch()
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.addStretch()
        case 'hbox_right':
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.addStretch()
        case "hbox_center":
            layout.addStretch()
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.addStretch()
        case 'vbox_customer_distance':
            if total_index >= item_location:
                reduce_index = abs(total_index - item_location)
                for i in range(reduce_index):
                    layout.addWidget(widgets[i])
                if item_location != 0:
                    layout.addStretch()
                    layout.addWidget(widgets[reduce_index])

                for j in range(item_location):
                    layout.addWidget(widgets[j])

            else:
                general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_factor':

            for i in range(len(widgets)):
                layout.addWidget(widgets[i])
                if type(total_index) == type(item_distance):
                    layout.setStretchFactor(widgets[i], item_distance)
                else:
                    assert (not isinstance(item_distance, int)), "item_distance must be a list or tuple"
                    if len(item_distance) == total_index:
                        layout.setStretchFactor(widgets[i], item_distance[i])
                    else:
                        general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_space':
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.setSpacing(space_distance)
        case 'vbox_margins':
            if margins is None:
                general_layout(widgets=widgets, self=self, layout=layout)
            elif len(margins) >= 4:
                margins = (0, 0, 0, 0)
                general_layout(widgets=widgets, self=self, layout=layout)
                layout.setContentsMargins(*margins)
        case 'hbox':
            general_layout(widgets=widgets, self=self, layout=layout)
        case "hbox_customer_distance":
            safe_offest = abs(total_index - item_location)
            if safe_offest > total_index:
                general_layout(widgets=widgets, self=self, layout=layout)
            else:
                for i in range(safe_offest):
                    layout.addWidget(widgets[i])
                    if type(total_index) == type(item_distance):
                        layout.setStretchFactor(widgets[i], item_distance)
                    else:
                        assert (not isinstance(item_distance, int)), "item_distance must be a list or tuple"
                        layout.setStretchFactor(widgets[i], item_distance[i])

        case "hbox_space":
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.setSpacing(space_distance)
        case "hbox_margins":
            general_layout(widgets=widgets, self=self, layout=layout)
            if margins is None:
                margins = (40, 40, 40, 40)
            elif len(margins) > 4:
                margins = (0, 0, 0, 0)
            layout.setContentsMargins(*margins)
        case 'grid':
            assert (isinstance(layout, QGridLayout)), "layout type is QGridLayout"
            if widget_position is None:
                general_layout(widgets=widgets, self=self, layout=layout)
            elif widget_position is not None:
                if len(widget_position) == total_index:
                    row_column = [(x[0], x[1]) for x in widget_position]
                    for i in range(total_index):
                        layout.addWidget(widgets[i], row_column[i][0], row_column[i][1], alignment=alignment[i])
                else:
                    general_layout(widgets=widgets, self=self, layout=layout)
        case 'form':
            assert len(element_name) == total_index, 'two variable length must be equal'
            assert (isinstance(layout, QFormLayout)), "layout type is QFormLayout"
            if len(element_name) == total_index:
                for i in range(total_index):
                    if not isinstance(widgets[i], QPushButton):
                        layout.addRow(element_name[i], widgets[i])

                    else:
                        layout.addRow(widgets[i])



            else:
                for i in range(total_index):
                    layout.addRow(widgets[i])

    self.setLayout(layout)


def complex_layout(main_layout: QGridLayout, paper_layout_widget: tuple[QWidget, QWidget],
                   tad_paper_name: tuple[str, str], Tad_layout: QTabWidget,
                   sub_layout: tuple[QFormLayout, QFormLayout], paper_one_element: tuple, paper_two_element: tuple,
                   setLayoutWidget: tuple, setLayout_Location: tuple, alignment: tuple, paper_one_widgets: tuple,
                   paper_two_widgets: tuple):
    altogether_sub_layout = len(sub_layout)

    assert altogether_sub_layout >= 2, "there must be at least 2 sub layouts"

    first_sub_layout, *middle_sub_layout, last_sub_layout = sub_layout

    widget_paper_one, *widget_paper_middle, widget_paper_two = paper_layout_widget
    if not widget_paper_middle:
        del widget_paper_middle
    if not middle_sub_layout:
        del middle_sub_layout

    assert len(paper_one_element + paper_two_element) == len(
        paper_one_widgets + paper_two_widgets), "total widget and element length must be equal"

    for item in range(len(paper_one_element)):
        first_sub_layout.addRow(paper_one_element[item], paper_one_widgets[item])
    for items in range(len(paper_two_element)):
        last_sub_layout.addRow(paper_two_element[items], paper_two_widgets[items])

    widget_paper_one.setLayout(first_sub_layout)
    widget_paper_two.setLayout(last_sub_layout)

    assert len(paper_layout_widget) == len(tad_paper_name)

    for tad_property in range(len(paper_layout_widget)):
        Tad_layout.addTab(paper_layout_widget[tad_property], tad_paper_name[tad_property])

    assert len(setLayout_Location) == len(setLayoutWidget) == len(alignment), "three parameter length must be equal"

    for grid_virtue in range(len(setLayoutWidget)):
        main_layout.addWidget(setLayoutWidget[grid_virtue], *setLayout_Location[grid_virtue],
                              alignment=alignment[grid_virtue])
