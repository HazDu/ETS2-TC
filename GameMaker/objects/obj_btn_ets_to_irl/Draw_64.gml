draw_self()

//text to draw
draw_text(x, y, "Euro Truck Time --> Real Time")

if(mouse_x >= bbox_left && mouse_x <= bbox_right && mouse_y >= bbox_top && mouse_y <= bbox_bottom && mouse_check_button_released(mb_left))
{
	window_set_cursor(cr_default)
	room_goto(rm_ets_to_irl)
}