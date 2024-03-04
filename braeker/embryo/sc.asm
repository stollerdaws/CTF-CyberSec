LOAD:08048007                 mov     al, 3
LOAD:08048009                 pop     ecx
LOAD:0804800A                 xor     cl, cl
LOAD:0804800C                 mov     dl, 12h
LOAD:0804800E                 int     80h
LOAD:08048010                 add     al, [eax]
LOAD:08048012                 add     eax, [eax]
LOAD:08048014                 add     [eax], eax

	mov al, 3
	pop ecx
	mov dl, 0xff
	xor ebx, ebx
	int 0x80
	call 0x0804800	

08048000	
