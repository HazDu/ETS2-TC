//autofocus
if(keyboard_check_pressed(vk_tab))
{
	global.autofocus++
}
if(global.autofocus >= 3)
{
	global.autofocus = 1
}

if(room == rm_ets_to_irl)
{
	draw_text(640, 130, "Euro Truck Hours:")
	
	draw_text(room_width/2, 330, "Euro Truck Minutes:")
	
	//set values to 0 if string has no input to not confuse real() function
	if(obj_input_box_1.custom_string == "")
	{
		value1 = 0
	}
	else
	{
		value1 = real(obj_input_box_1.custom_string)
	}
	
	if(obj_input_box_2.custom_string == "")
	{
		value2 = 0
	}
	else
	{
		value2 = real(obj_input_box_2.custom_string)
	}
	
	//draw Result
	draw_set_halign(fa_left)
	draw_text(30, 650, value1)
	draw_text(30, 700, value2)
	draw_set_halign(fa_center)
}
