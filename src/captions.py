class Captions:
    
    @classmethod
    def convert_time_to_subtitle(cls, seconds_left: float):
        minutes = 0
        hours = 0
        while True:
            if seconds_left - 60 <= 0:
                break
            else:
                seconds_left -= 60
                minutes += 1
                if minutes - 60 <= 0:
                    minutes -= 0
                    hours += 1
                print(seconds_left)
                print(minutes)
                print(hours)
        true_seconds = f"{str(seconds_left).split(".")[0]:{"0"}>2}"
        true_ms = f"{float("0." + str(seconds_left).split(".")[1]):.3f}".split(".")[1]
        if len(str(hours)) <= 2:
            return f"{hours:02}:{minutes:02}:{true_seconds}.{true_ms}"
        else:
            return f"{hours}:{minutes:02}:{true_seconds}.{true_ms}"
    
    @classmethod
    def convert_temp_to_captions(cls, temp: str, capt_type: str="vtt") -> str:
        # make a blank new captions variable
        current_captions = ""
        if capt_type == "vtt":
            # Required under the VTT standard
            current_captions = "WEBVTT\n\n"
            is_in_segment = False
            is_first = False
            start_line = ""
            end_line = ""
            word_list = []
            for line in temp.splitlines():
                if line.endswith(":") and not line.startswith("  "):
                    if is_in_segment:
                        is_in_segment = False
                        current_captions = current_captions + f"{start_line} --> {end_line}\n{" ".join(word_list)}\n\n"
                        word_list = []
                    current_captions = current_captions + str(int(line.split(":")[0]) + 1)  + "\n"
                    is_in_segment = True
                    is_first = True
                    start_line = ""
                elif line.startswith("  ") and is_in_segment:
                    if is_first:
                        is_first = False
                        time = line.split(":")[0].split("/")[0]
                        seconds_left = float(time)
                        start_line = cls.convert_time_to_subtitle(seconds_left)
                        word_list.append(line.split(": ")[-1])
                    else:
                        word_list.append(line.split(": ")[-1])
                        end_line = cls.convert_time_to_subtitle(float(line.split(": ")[0].split("/")[1]))
            is_in_segment = False
            current_captions = current_captions + f"{start_line} --> {end_line}\n{" ".join(word_list)}\n"
            word_list = []
        return current_captions
with open("C:/Users/Zachary.Smith/OneDrive - Hutto ISD/Coding/WIN_20260211_11_56_52_Pro.mp4_transcript.txt", 'r') as file:
   item = file.read()
   file.close()

print(Captions.convert_temp_to_captions(item))