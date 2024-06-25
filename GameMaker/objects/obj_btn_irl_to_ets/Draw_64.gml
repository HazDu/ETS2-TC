draw_self()

//text to draw
draw_text(x, y, "Real Time --> Euro Truck Time")

//check if button is pressed
if(mouse_x >= bbox_left && mouse_x <= bbox_right && mouse_y >= bbox_top && mouse_y <= bbox_bottom && mouse_check_button_released(mb_left))
{
	window_set_cursor(cr_default)
	room_goto(rm_irl_to_ets)
}