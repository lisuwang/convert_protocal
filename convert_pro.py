#import json
def convert_protocol(action, dataType, src):
    to = {}
    li = action.split(':')
    li_left = li[0]
    li_right = li[1]
    if len(li) % 2 != 0:
        return False
    else:
        li_to_str = lambda li : ''.join(e for e in li)
        li_left_str = li_to_str(li_left)
        li_right_str = li_to_str(li_right)
        left = li_left_str.split(',')
        right = li_right_str.split(',')
        if len(left) != len(right):
            return False
        else:
            i = 0
            while i != len(left):
                ob_from =src
                ob_to = to
                tmp_right = right[i].strip(' ').split('|')
                tmp_left = left[i].strip(' ').split('|')
                for z in tmp_right:
                    if z in ob_from:
                        ob_from = ob_from[z]
                    else:
                        return False
                count = 0
                for z in tmp_left:
                    count += 1
                    if z in ob_to:
                        ob_to = ob_to[z]
                    else:
                        ob_to[z] = {}
                        if count == len(tmp_left):
                            ob_to[z] = ob_from
                        else:
                            ob_to = ob_to[z]

                i = i + 1
    return to
          
if __name__ == "__main__":

    val = {
        "ID": "1",
        "Type": "scr_type",
        "Factory": {
            "ID": "001-002",
            "Address": "Orleans-oldMill-1-101",
            "Manager": {
                "ID": "002",
                "Name": "Joan Mary"
            },
            "Name": "deak lamp",
            "Weight": "200g",
            "Material": {
                "M1": "Fe",
                "M2": "wire",
                "M3": "Cu"
            }
        },
        "DateOfManufacture": "2019-08-01 8:15 AM"
    }
    str="ID,Property|Type,Property|Weight,Property|Company|ID,Property|Company|Address,Property|Company|Manager|ID,Property|Company|Manager|Name,Property|Name,Property|M1,Property|M2,Property|M3,DateOfManufacture" \
            ":" \
            "ID,Type,Factory|Weight,Factory|ID,Factory|Address,Factory|Manager|ID,Factory|Manager|Name,Factory|Name,Factory|Material|M1,Factory|Material|M2,Factory|Material|M3,DateOfManufacture"
    to = {}
    to = convert_protocol(str, 'WordsHelpYouReCall', val)
    #print(json.dumps(to, indent = True), end='\n')
