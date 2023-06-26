
 Copyright 2023 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 "encoder.py":5
 * import binascii
 * 
 * def hexstr_to_binstr(hexstr):             # <<<<<<<<<<<<<<
 *     n = int(hexstr, 16)
 *     bstr = ''
 "encoder.py":6
 * 
 * def hexstr_to_binstr(hexstr):
 *     n = int(hexstr, 16)             # <<<<<<<<<<<<<<
 *     bstr = ''
 *     while n > 0:
 "encoder.py":7
 * def hexstr_to_binstr(hexstr):
 *     n = int(hexstr, 16)
 *     bstr = ''             # <<<<<<<<<<<<<<
 *     while n > 0:
 *         bstr = str(n % 2) + bstr
 "encoder.py":8
 *     n = int(hexstr, 16)
 *     bstr = ''
 *     while n > 0:             # <<<<<<<<<<<<<<
 *         bstr = str(n % 2) + bstr
 *         n = n >> 1
 "encoder.py":9
 *     bstr = ''
 *     while n > 0:
 *         bstr = str(n % 2) + bstr             # <<<<<<<<<<<<<<
 *         n = n >> 1
 *     if len(bstr) % 8 != 0:
 "encoder.py":10
 *     while n > 0:
 *         bstr = str(n % 2) + bstr
 *         n = n >> 1             # <<<<<<<<<<<<<<
 *     if len(bstr) % 8 != 0:
 *         bstr = '0' + bstr
 "encoder.py":11
 *         bstr = str(n % 2) + bstr
 *         n = n >> 1
 *     if len(bstr) % 8 != 0:             # <<<<<<<<<<<<<<
 *         bstr = '0' + bstr
 *     return bstr
 "encoder.py":12
 *         n = n >> 1
 *     if len(bstr) % 8 != 0:
 *         bstr = '0' + bstr             # <<<<<<<<<<<<<<
 *     return bstr
 * 
 "encoder.py":11
 *         bstr = str(n % 2) + bstr
 *         n = n >> 1
 *     if len(bstr) % 8 != 0:             # <<<<<<<<<<<<<<
 *         bstr = '0' + bstr
 *     return bstr
 "encoder.py":13
 *     if len(bstr) % 8 != 0:
 *         bstr = '0' + bstr
 *     return bstr             # <<<<<<<<<<<<<<
 * 
 * 
 "encoder.py":5
 * import binascii
 * 
 * def hexstr_to_binstr(hexstr):             # <<<<<<<<<<<<<<
 *     n = int(hexstr, 16)
 *     bstr = ''
 "encoder.py":16
 * 
 * 
 * def pixel_bit(b):             # <<<<<<<<<<<<<<
 *     return tuple((0, 1, b))
 * 
 "encoder.py":17
 * 
 * def pixel_bit(b):
 *     return tuple((0, 1, b))             # <<<<<<<<<<<<<<
 * 
 * 
 "encoder.py":16
 * 
 * 
 * def pixel_bit(b):             # <<<<<<<<<<<<<<
 *     return tuple((0, 1, b))
 * 
 "encoder.py":20
 * 
 * 
 * def embed(t1, t2):             # <<<<<<<<<<<<<<
 *     return tuple((t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]))
 * 
 "encoder.py":21
 * 
 * def embed(t1, t2):
 *     return tuple((t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]))             # <<<<<<<<<<<<<<
 * 
 * 
 "encoder.py":20
 * 
 * 
 * def embed(t1, t2):             # <<<<<<<<<<<<<<
 *     return tuple((t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]))
 * 
 "encoder.py":24
 * 
 * 
 * def full_pixel(pixel):             # <<<<<<<<<<<<<<
 *     return pixel[1] == 255 or pixel[2] == 255
 * 
 "encoder.py":25
 * 
 * def full_pixel(pixel):
 *     return pixel[1] == 255 or pixel[2] == 255             # <<<<<<<<<<<<<<
 * 
 * print("Embedding file...")
 "encoder.py":24
 * 
 * 
 * def full_pixel(pixel):             # <<<<<<<<<<<<<<
 *     return pixel[1] == 255 or pixel[2] == 255
 * 
 "encoder.py":5
 * import binascii
 * 
 * def hexstr_to_binstr(hexstr):             # <<<<<<<<<<<<<<
 *     n = int(hexstr, 16)
 *     bstr = ''
 "encoder.py":16
 * 
 * 
 * def pixel_bit(b):             # <<<<<<<<<<<<<<
 *     return tuple((0, 1, b))
 * 
 "encoder.py":20
 * 
 * 
 * def embed(t1, t2):             # <<<<<<<<<<<<<<
 *     return tuple((t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]))
 * 
 "encoder.py":24
 * 
 * 
 * def full_pixel(pixel):             # <<<<<<<<<<<<<<
 *     return pixel[1] == 255 or pixel[2] == 255
 * 
 "encoder.py":29
 * print("Embedding file...")
 * 
 * bin_data = open("./flag.txt", 'rb').read()             # <<<<<<<<<<<<<<
 * data_to_hide = binascii.hexlify(bin_data).decode('utf-8')
 * 
 "encoder.py":30
 * 
 * bin_data = open("./flag.txt", 'rb').read()
 * data_to_hide = binascii.hexlify(bin_data).decode('utf-8')             # <<<<<<<<<<<<<<
 * 
 * base_image = Image.open("./original.png")
 "encoder.py":32
 * data_to_hide = binascii.hexlify(bin_data).decode('utf-8')
 * 
 * base_image = Image.open("./original.png")             # <<<<<<<<<<<<<<
 * 
 * x_len, y_len = base_image.size
 "encoder.py":55
 *         if remaining_bits > 0 and next_position <= 0 and not full_pixel(pixel):
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)
 *             next_position = randint(1, 17)             # <<<<<<<<<<<<<<
 *             binary_string = binary_string[1:]
 *             remaining_bits -= 1
 "encoder.py":56
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)
 *             next_position = randint(1, 17)
 *             binary_string = binary_string[1:]             # <<<<<<<<<<<<<<
 *             remaining_bits -= 1
 *         else:
 "encoder.py":63
 * 
 * 
 * new_image.save("./symatrix.png")             # <<<<<<<<<<<<<<
 * new_image.close()
 * base_image.close()
 "encoder.py":68
 * 
 * print("Work done!")
 * exit(1)             # <<<<<<<<<<<<<<
 "encoder.py":1
 * from PIL import Image             # <<<<<<<<<<<<<<
 * from random import randint
 * import binascii
 "encoder.py":2
 * from PIL import Image
 * from random import randint             # <<<<<<<<<<<<<<
 * import binascii
 * 
 "encoder.py":3
 * from PIL import Image
 * from random import randint
 * import binascii             # <<<<<<<<<<<<<<
 * 
 * def hexstr_to_binstr(hexstr):
 "encoder.py":5
 * import binascii
 * 
 * def hexstr_to_binstr(hexstr):             # <<<<<<<<<<<<<<
 *     n = int(hexstr, 16)
 *     bstr = ''
 "encoder.py":16
 * 
 * 
 * def pixel_bit(b):             # <<<<<<<<<<<<<<
 *     return tuple((0, 1, b))
 * 
 "encoder.py":20
 * 
 * 
 * def embed(t1, t2):             # <<<<<<<<<<<<<<
 *     return tuple((t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2]))
 * 
 "encoder.py":24
 * 
 * 
 * def full_pixel(pixel):             # <<<<<<<<<<<<<<
 *     return pixel[1] == 255 or pixel[2] == 255
 * 
 "encoder.py":27
 *     return pixel[1] == 255 or pixel[2] == 255
 * 
 * print("Embedding file...")             # <<<<<<<<<<<<<<
 * 
 * bin_data = open("./flag.txt", 'rb').read()
 "encoder.py":29
 * print("Embedding file...")
 * 
 * bin_data = open("./flag.txt", 'rb').read()             # <<<<<<<<<<<<<<
 * data_to_hide = binascii.hexlify(bin_data).decode('utf-8')
 * 
 "encoder.py":30
 * 
 * bin_data = open("./flag.txt", 'rb').read()
 * data_to_hide = binascii.hexlify(bin_data).decode('utf-8')             # <<<<<<<<<<<<<<
 * 
 * base_image = Image.open("./original.png")
 "encoder.py":32
 * data_to_hide = binascii.hexlify(bin_data).decode('utf-8')
 * 
 * base_image = Image.open("./original.png")             # <<<<<<<<<<<<<<
 * 
 * x_len, y_len = base_image.size
 "encoder.py":34
 * base_image = Image.open("./original.png")
 * 
 * x_len, y_len = base_image.size             # <<<<<<<<<<<<<<
 * nx_len = x_len * 2
 * 
 "encoder.py":35
 * 
 * x_len, y_len = base_image.size
 * nx_len = x_len * 2             # <<<<<<<<<<<<<<
 * 
 * new_image = Image.new("RGB", (nx_len, y_len))
 "encoder.py":37
 * nx_len = x_len * 2
 * 
 * new_image = Image.new("RGB", (nx_len, y_len))             # <<<<<<<<<<<<<<
 * 
 * base_matrix = base_image.load()
 "encoder.py":39
 * new_image = Image.new("RGB", (nx_len, y_len))
 * 
 * base_matrix = base_image.load()             # <<<<<<<<<<<<<<
 * new_matrix = new_image.load()
 * 
 "encoder.py":40
 * 
 * base_matrix = base_image.load()
 * new_matrix = new_image.load()             # <<<<<<<<<<<<<<
 * 
 * binary_string = hexstr_to_binstr(data_to_hide)
 "encoder.py":42
 * new_matrix = new_image.load()
 * 
 * binary_string = hexstr_to_binstr(data_to_hide)             # <<<<<<<<<<<<<<
 * remaining_bits = len(binary_string)
 * 
 "encoder.py":43
 * 
 * binary_string = hexstr_to_binstr(data_to_hide)
 * remaining_bits = len(binary_string)             # <<<<<<<<<<<<<<
 * 
 * nx_len = nx_len - 1
 "encoder.py":45
 * remaining_bits = len(binary_string)
 * 
 * nx_len = nx_len - 1             # <<<<<<<<<<<<<<
 * next_position = 0
 * 
 "encoder.py":46
 * 
 * nx_len = nx_len - 1
 * next_position = 0             # <<<<<<<<<<<<<<
 * 
 * for i in range(0, y_len):
 "encoder.py":48
 * next_position = 0
 * 
 * for i in range(0, y_len):             # <<<<<<<<<<<<<<
 *     for j in range(0, x_len):
 * 
 "encoder.py":49
 * 
 * for i in range(0, y_len):
 *     for j in range(0, x_len):             # <<<<<<<<<<<<<<
 * 
 *         pixel = new_matrix[j, i] = base_matrix[j, i]
 "encoder.py":51
 *     for j in range(0, x_len):
 * 
 *         pixel = new_matrix[j, i] = base_matrix[j, i]             # <<<<<<<<<<<<<<
 * 
 *         if remaining_bits > 0 and next_position <= 0 and not full_pixel(pixel):
 "encoder.py":53
 *         pixel = new_matrix[j, i] = base_matrix[j, i]
 * 
 *         if remaining_bits > 0 and next_position <= 0 and not full_pixel(pixel):             # <<<<<<<<<<<<<<
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)
 *             next_position = randint(1, 17)
 "encoder.py":54
 * 
 *         if remaining_bits > 0 and next_position <= 0 and not full_pixel(pixel):
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)             # <<<<<<<<<<<<<<
 *             next_position = randint(1, 17)
 *             binary_string = binary_string[1:]
 "encoder.py":55
 *         if remaining_bits > 0 and next_position <= 0 and not full_pixel(pixel):
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)
 *             next_position = randint(1, 17)             # <<<<<<<<<<<<<<
 *             binary_string = binary_string[1:]
 *             remaining_bits -= 1
 "encoder.py":56
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)
 *             next_position = randint(1, 17)
 *             binary_string = binary_string[1:]             # <<<<<<<<<<<<<<
 *             remaining_bits -= 1
 *         else:
 "encoder.py":57
 *             next_position = randint(1, 17)
 *             binary_string = binary_string[1:]
 *             remaining_bits -= 1             # <<<<<<<<<<<<<<
 *         else:
 *             new_matrix[nx_len - j, i] = pixel
 "encoder.py":53
 *         pixel = new_matrix[j, i] = base_matrix[j, i]
 * 
 *         if remaining_bits > 0 and next_position <= 0 and not full_pixel(pixel):             # <<<<<<<<<<<<<<
 *             new_matrix[nx_len - j, i] = embed(pixel_bit(int(binary_string[0])),pixel)
 *             next_position = randint(1, 17)
 "encoder.py":59
 *             remaining_bits -= 1
 *         else:
 *             new_matrix[nx_len - j, i] = pixel             # <<<<<<<<<<<<<<
 *             next_position -= 1
 * 
else*/ {
        __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_pixel); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_new_matrix); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_10);
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_nx_len); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_j); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_11 = PyNumber_Subtract(__pyx_t_12, __pyx_t_2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_i); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_12 = PyTuple_New(2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_GIVEREF(__pyx_t_11);
        PyTuple_SET_ITEM(__pyx_t_12, 0, __pyx_t_11);
        __Pyx_GIVEREF(__pyx_t_2);
        PyTuple_SET_ITEM(__pyx_t_12, 1, __pyx_t_2);
        __pyx_t_11 = 0;
        __pyx_t_2 = 0;
        if (unlikely(PyObject_SetItem(__pyx_t_10, __pyx_t_12, __pyx_t_16) < 0)) __PYX_ERR(0, 59, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;

 "encoder.py":60
 *         else:
 *             new_matrix[nx_len - j, i] = pixel
 *             next_position -= 1             # <<<<<<<<<<<<<<
 * 
 * 
 "encoder.py":49
 * 
 * for i in range(0, y_len):
 *     for j in range(0, x_len):             # <<<<<<<<<<<<<<
 * 
 *         pixel = new_matrix[j, i] = base_matrix[j, i]
 "encoder.py":48
 * next_position = 0
 * 
 * for i in range(0, y_len):             # <<<<<<<<<<<<<<
 *     for j in range(0, x_len):
 * 
 "encoder.py":63
 * 
 * 
 * new_image.save("./symatrix.png")             # <<<<<<<<<<<<<<
 * new_image.close()
 * base_image.close()
 "encoder.py":64
 * 
 * new_image.save("./symatrix.png")
 * new_image.close()             # <<<<<<<<<<<<<<
 * base_image.close()
 * 
 "encoder.py":65
 * new_image.save("./symatrix.png")
 * new_image.close()
 * base_image.close()             # <<<<<<<<<<<<<<
 * 
 * print("Work done!")
 "encoder.py":67
 * base_image.close()
 * 
 * print("Work done!")             # <<<<<<<<<<<<<<
 * exit(1)
 "encoder.py":68
 * 
 * print("Work done!")
 * exit(1)             # <<<<<<<<<<<<<<
 "encoder.py":1
 * from PIL import Image             # <<<<<<<<<<<<<<
 * from random import randint
 * import binascii
 _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
 XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
 function called with no arguments, but all parameters have
 If the code object creation fails, then we should clear the
 the line below is just to avoid C compiler
