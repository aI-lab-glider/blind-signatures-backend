import functools
import hashlib
import ecdsa

from ecdsa.ecdsa import curve_secp256k1
from ecdsa.curves import SECP256k1
from ecdsa import numbertheory


def verify_ring_signature(message, y, signature, G=SECP256k1.generator, hash_func=hashlib.sha3_256):

    c_0 = signature[0]
    s = signature[1:-2]
    Y = ecdsa.ellipticcurve.Point(curve_secp256k1, signature[-2], signature[-1])
    n = len(y)
    c = [c_0] + [0] * (n - 1)

    H = H2(y, hash_func=hash_func)

    for i in range(n):
        z_1 = (G * s[i]) + (y[i] * c[i])
        z_2 = (H * s[i]) + (Y * c[i])

        if i < n - 1:
            c[i + 1] = H1([y, Y, message, z_1, z_2], hash_func=hash_func)
        else:
            return c_0 == H1([y, Y, message, z_1, z_2], hash_func=hash_func)

    return False


def map_to_curve(x, P=curve_secp256k1.p()):
    x -= 1
    y = 0
    found = False

    while not found:
        x += 1
        f_x = (x * x * x + 7) % P

        try:
            y = numbertheory.square_root_mod_prime(f_x, P)
            found = True
        except Exception as e:
            pass

    return ecdsa.ellipticcurve.Point(curve_secp256k1, x, y)


def H1(msg, hash_func=hashlib.sha3_256):
    return int('0x'+ hash_func(concat(msg).encode()).hexdigest(), 16)


def H2(msg, hash_func=hashlib.sha3_256):
    return map_to_curve(H1(msg, hash_func=hash_func))


def concat(params):
    n = len(params)
    bytes_value = [0] * n

    for i in range(n):

        if type(params[i]) is int:
            bytes_value[i] = hashlib.sha3_256(str(params[i]).encode()).hexdigest()
        if type(params[i]) is list:
            bytes_value[i] = concat(params[i])
        if type(params[i]) is ecdsa.ellipticcurve.Point:
            a = str(params[i].x())
            b = str(params[i].y())
            bytes_value[i] = hashlib.sha3_256((a + b).encode()).hexdigest()
        if type(params[i]) is str:
            bytes_value[i] = hashlib.sha3_256(params[i].encode()).hexdigest()

        if bytes_value[i] == 0:
            a = str(params[i].x())
            b = str(params[i].y())
            bytes_value[i] = hashlib.sha3_256((a + b).encode()).hexdigest()

    return functools.reduce(lambda x, y: x + y, bytes_value)



private_keys = [6258797722142887902326437776644082295381852716177135942667414549377913946638,
                21395736402384775696845026906418732552219621898540192789380606916173329157561,
                86439457609385391029859866191902459201595587903113443789569434595663993587029,
                10847031540638908869647665033049572579030779063314235603902587403290407360655,
                3906468134155590009746309495400846138926361677290608255207289551900279089753,
                113950188096694274038398247823598447727918190636938212643311477829355552363944,
                78035251763106983647079993948427073480337638968063482805867273010610805492488,
                31124367021094598295621189662213550590171531228372889439526436492507895319041,
                3311400462234423981996386759691180399731141366166246619614281589344135573928,
                83987342557096576049999536116587801242570673256937548822415817489971991458545]
public_keys = list(map(lambda xi: SECP256k1.generator * xi, private_keys))
message = "hello"
signature = [12211534182106933616787808968209174524304622822258502447123132503882101245911, 105369868767627699677869220810374935049922690532231816529990838927657967618028, 90936476144785548610461775202356510235310070064644951990174239773049997297913, 109154562926251335403388055140973848997029375793306218096036054532583441503408, 34864493780537132985657906483485499340986049256394343217764704322348820595164, 58125235570565953412101405467351847854923043981198938242141655387629480839982, 78550846324642717225010931322963450080616444460188238059950195944100402924292, 59141826375594792593171203770773315471262621443158725448332923087795673939780, 102487697288034044756942705465375622729893878505194854473869184044324265894140, 70322996469270179830478546435840334511587664181254016228332869034665985158367, 112806217163963724054887237205946396598873675362788368455328479468125864381588, 13975964809536264569204613225328127553933143866259625575854614640099269906607, 49967853652717693353636203623330956742505180517566137542747695874788946393447]
assert (verify_ring_signature(message, public_keys, signature))
