blob = """I come in peace.
Prepare to be destroyed!
                                  �YxâWC?+ �($�>2{�te�BR7<�:�Ͼ�������h�^�r����v`J8��f8�@�)y�jH�#Zw�bjZ�L՟&uiA-
��K���e&[ 	J�٣�������������xP�M��"""

from hashlib import sha256
print(blob.splitlines()[0])
# z = sha256(blob.splitlines()[2]).hexdigest()
# i = int(z, 16)
#
# if(z%2 == 0):
#   print(blob.splitlines()[0])
# else:
#   print(blob.splitlines()[1])
