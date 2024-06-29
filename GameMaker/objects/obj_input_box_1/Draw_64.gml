draw_self()

//check if box is clicked
if(mouse_x >= bbox_left && mouse_x <= bbox_right && mouse_y >= bbox_top && mouse_y <= bbox_bottom && mouse_check_button(mb_left))
{
	global.autofocus = 1
}

//check if box is focused
if(global.autofocus == 1)
{
	//change sprite
	image_index = 1
	
	//build string
	if(keyboard_check_pressed(vk_anykey) && (keyboard_lastchar >= "0" && keyboard_lastchar <= "9") && string_length(custom_string) < 20)
	{
		custom_string = string_insert(keyboard_lastchar, custom_string, string_length(custom_string) + 1)
	}
	
	//delete last char
	if(keyboard_check_pressed(vk_backspace))
	{
		custom_string = string_delete(custom_string, string_length(custom_string), 1)
	}
	
	//delete everything
	if(keyboard_check_pressed(vk_delete))
	{
		custom_string = ""
	}
}
else
{
	//change sprite
	image_index = 0
	cursor = ""
}

//draw string
draw_set_halign(fa_left)
draw_text(x - 280, y, custom_string + cursor)
draw_set_halign(fa_center)