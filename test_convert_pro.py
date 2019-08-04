import json
import convert_pro

if __name__ == '__main__':
    val = {
        "ID":"42",
        "Message":"Sooner is better than as later",
        "Layer":"1"
    }

    goal = {
        "First":{
            "ID":"42",
            "Message":"Sooner is better than as later",
            "Layer":"1"
        }
    }

    policy1 = "First|ID, First|Message, First|Layer:ID,Message,Layer"
    to = convert_pro.convert_protocol(policy1,"simple_test_1", val)
    assert(goal["First"]["ID"] == to["First"]["ID"])
    assert(val["ID"] == to["First"]["ID"])
    assert(goal["First"]["Message"] == to["First"]["Message"])
    assert(val["Message"] == to["First"]["Message"])
    assert(goal["First"]["Layer"] == to["First"]["Layer"])
    assert(val["Layer"] == to["First"]["Layer"])
    assert(json.dumps(to) == json.dumps(goal))
    print (json.dumps(to, indent = True))

