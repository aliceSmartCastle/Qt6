import typing

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout


def layout_setting(layout: QVBoxLayout | QHBoxLayout, *widgets) -> None:
    """
    add widgets to layout
    """
    # self.setLayout(layout)

    for makes in range(len(widgets)):
        layout.addWidget(widgets[makes])


def general_layout(widgets: tuple, self: QWidget, layout: typing.Union[QVBoxLayout, QHBoxLayout]):
    layout_setting(layout, *widgets)
    self.setLayout(layout)


def layout_modes(widgets: tuple | list, self: QWidget, layout: typing.Union[QVBoxLayout, QHBoxLayout],
                 mode: typing.Literal[
                     'vbox', 'vbox_top', 'vbox_down', 'vbox_center', 'vbox_factor', 'vbox_customer_distance', 'vbox_space',
                     'hbox', 'hbox_left', 'hbox_right', 'hbox_center', 'hbox_customer_distance', 'hbox_space', 'hbox_margins', 'vbox_margins'] = 'vbox'
                 , item_location: int = 0, item_distance: typing.Union[list[int], tuple[int]] = None,
                 space_distance: int = 10,
                 margins: tuple[int, int, int, int] = None):
    total_index = len(widgets)
    if item_distance is None:
        lad_list = [i for i in range(total_index)]
        item_distance = round(sum(lad_list) / len(lad_list))

    match mode:

        case 'vbox':
            general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_down':
            layout.addStretch()
            general_layout(widgets=widgets, self=self, layout=layout)
        case 'vbox_top':
            general_layout(widgets=widgets, self=self, layout=layout)
            layout.addStretch()
        case 'hbox_left':
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
            elif len(margins) > 4:
                margins = (0, 0, 0, 0)
            layout.setContentsMargins(*margins)
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
    self.setLayout(layout)
