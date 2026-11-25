from pass_requirement import PassReq
from generator import PassGen

while True:

    pass_req = PassReq()
    reqs = pass_req.return_req()

    gen = PassGen(reqs)
    print("Password Generated: ", gen.generate())

    another_pass = input("Another one?: (y/n)").strip().lower()
    if another_pass != "y":
        break