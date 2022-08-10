
def yolo_pseudo_conf(yolo_format, pseudo_conf=1):
    # l should be [<class_index>, <rel_x_center>, <rel_y_center>, <rel_bbox_w>, <rel_bbox_h>]
    l = yolo_format.split(" ")

    return f"{l[0]} {pseudo_conf} {l[1]} {l[2]} {l[3]} {l[4]}"