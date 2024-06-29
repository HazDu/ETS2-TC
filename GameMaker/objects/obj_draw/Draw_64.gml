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
	draw_text(room_width/2, 130, "Euro Truck Hours:")
	
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
	
	//calculate ets to irl time
	temp_min = value2 + (value1 * 60)
	temp_min = temp_min / 19
	value1 = floor(temp_min / 60)
	value2 = round(temp_min % 60)
	
	//draw Result
	draw_text(room_width/2, 580, "That's " + string(value1) + " hours and " + string(value2) + " minutes in real time.")
}

if(room == rm_irl_to_ets)
{
	draw_text(room_width/2, 130, "Real Time Hours:")
	
	draw_text(room_width/2, 330, "Real Time Minutes:")
	
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
	
	//calculate ets to irl time
	temp_min = value2 + (value1 * 60)
	temp_min = temp_min * 19
	value1 = floor(temp_min / 60)
	value2 = round(temp_min % 60)
	
	//draw Result
	draw_text(room_width/2, 580, "That's " + string(value1) + " hours and " + string(value2) + " minutes in Euro Truck Simulator 2.")
}
