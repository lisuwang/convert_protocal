import json
import convert_pro
import unittest

class TestSimpleConvertProtocal(unittest.TestCase):
    def test_1_layer_convert_protocal(self):
        policy1 = "First|ID, First|Message, First|Layer:ID,Message,Layer"
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
        to = convert_pro.convert_protocol(policy1,"simple_test_1", val)
        assert(goal["First"]["ID"] == to["First"]["ID"])
        assert(val["ID"] == to["First"]["ID"])
        assert(goal["First"]["Message"] == to["First"]["Message"])
        assert(val["Message"] == to["First"]["Message"])
        assert(goal["First"]["Layer"] == to["First"]["Layer"])
        assert(val["Layer"] == to["First"]["Layer"])
        assert(json.dumps(to) == json.dumps(goal))
        #print (json.dumps(to, indent = True))

    def test_2_layer_convert_protocal(self):
        policy1 = "First|Second|ID, First|Second|Message, First|Second|Layer:ID,Message,Layer"
        val = {
            "ID":"42",
            "Message":"Sooner is better than as later",
            "Layer":"1"
        }

        goal = {
            "First":{
                "Second":{
                    "ID":"42",
                    "Message":"Sooner is better than as later",
                    "Layer":"1"
                }
            }
        }
        to = convert_pro.convert_protocol(policy1,"simple_test_2", val)
        assert(goal["First"]["Second"]["ID"] == to["First"]["Second"]["ID"])
        assert(val["ID"] == to["First"]["Second"]["ID"])
        assert(goal["First"]["Second"]["Message"] == to["First"]["Second"]["Message"])
        assert(val["Message"] == to["First"]["Second"]["Message"])
        assert(goal["First"]["Second"]["Layer"] == to["First"]["Second"]["Layer"])
        assert(val["Layer"] == to["First"]["Second"]["Layer"])
        assert(json.dumps(to) == json.dumps(goal))
        #print (json.dumps(to, indent = True))
    def test_complex_layer_convert_protocal_1(self):
        policy1 = "ID,Property|Type,Property|Weight,Property|Company|ID,Property|Company|Address,Property|Company|Manager|ID,Property|Company|Manager|Name,Property|Name,Property|M1,Property|M2,Property|M3,DateOfManufacture" \
            ":" \
            "ID,Type,Factory|Weight,Factory|ID,Factory|Address,Factory|Manager|ID,Factory|Manager|Name,Factory|Name,Factory|Material|M1,Factory|Material|M2,Factory|Material|M3,DateOfManufacture"
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

        goal = {
            "ID": "1",
            "Property":{
                "Type": "scr_type",
                "Company": {
                    "ID": "001-002",
                    "Address": "Orleans-oldMill-1-101",
                    "Manager": {
                        "ID": "002",
                        "Name": "Joan Mary"
                    }
                },
                "Name": "deak lamp",
                "Weight": "200g",
                "M1": "Fe",
                "M2": "wire",
                "M3": "Cu",
            },
            "DateOfManufacture": "2019-08-01 8:15 AM"
        }
        to = convert_pro.convert_protocol(policy1,"simple_test_3", val)
        assert(goal["ID"] == to["ID"])
        assert(goal["Property"]["Type"] == to["Property"]["Type"])
        assert(to["Property"]["Type"] == "scr_type")
        assert(goal["Property"]["Company"]["ID"] == to["Property"]["Company"]["ID"])
        assert(to["Property"]["Company"]["ID"] == "001-002")
        assert(goal["Property"]["Company"]["Manager"]["ID"] == to["Property"]["Company"]["Manager"]["ID"])
        assert(to["Property"]["Company"]["Manager"]["ID"] == "002")

        assert(to["Property"]["Name"] == "deak lamp")
        assert(to["Property"]["Weight"] == "200g")
        assert(to["Property"]["M1"] == "Fe")
        assert(to["Property"]["M2"] == "wire")
        assert(to["Property"]["M3"] == "Cu")
        assert(json.dumps(to,sort_keys=True) == json.dumps(goal,sort_keys=True))

    def test_complex_layer_convert_protocal_2(self):
        '''the opposite test case to prior one'''
        policy1 = "ID,Type,Factory|Weight,Factory|ID,Factory|Address,Factory|Manager|ID,Factory|Manager|Name,Factory|Name,Factory|Material|M1,Factory|Material|M2,Factory|Material|M3,DateOfManufacture" \
            ":" \
            "ID,Property|Type,Property|Weight,Property|Company|ID,Property|Company|Address,Property|Company|Manager|ID,Property|Company|Manager|Name,Property|Name,Property|M1,Property|M2,Property|M3,DateOfManufacture"
        val = {
            "ID": "1",
            "Property":{
                "Type": "scr_type",
                "Company": {
                    "ID": "001-002",
                    "Address": "Orleans-oldMill-1-101",
                    "Manager": {
                        "ID": "002",
                        "Name": "Joan Mary"
                    }
                },
                "Name": "deak lamp",
                "Weight": "200g",
                "M1": "Fe",
                "M2": "wire",
                "M3": "Cu",
            },
            "DateOfManufacture": "2019-08-01 8:15 AM"
        }

        goal = {
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
        to = convert_pro.convert_protocol(policy1,"simple_test_3", val)
        assert(goal["ID"] == to["ID"])
        assert(goal["Type"] == to["Type"])
        assert(to["Type"] == "scr_type")
        assert(goal["Factory"]["ID"] == to["Factory"]["ID"])
        assert(to["Factory"]["ID"] == "001-002")
        assert(goal["Factory"]["Manager"]["ID"] == to["Factory"]["Manager"]["ID"])
        assert(to["Factory"]["Manager"]["ID"] == "002")

        assert(to["Factory"]["Name"] == "deak lamp")
        assert(to["Factory"]["Weight"] == "200g")
        assert(to["Factory"]["Material"]["M1"] == "Fe")
        assert(to["Factory"]["Material"]["M2"] == "wire")
        assert(to["Factory"]["Material"]["M3"] == "Cu")
        assert(json.dumps(to,indent= True, sort_keys=True) == json.dumps(goal,indent= True, sort_keys=True))
        #print (json.dumps(to, indent = True))
if __name__ == '__main__':
    unittest.main()

