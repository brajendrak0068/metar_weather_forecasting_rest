from metar import Metar


def convert(text):
    output_res_dict = {}
    bytes_text = text.splitlines()[1] #split the response by newline and get the second element
    string_text = bytes_text.decode("utf-8")  #convert bytes to string literal

    metar_response = Metar.Metar( string_text )
    metar_response  = metar_response.string();
    metar_response = metar_response.splitlines()

    for s in metar_response:
        results  = s.split(':',1) 
        if len(results) > 1:
            output_res_dict[results[0]] = results[1]

    return output_res_dict

