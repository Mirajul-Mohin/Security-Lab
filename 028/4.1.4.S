.global your_asm_fn
.section .text

.section .data
	mp: .string "coolfood"
	sec: .int 0xc105ed

your_asm_fn:

push	%ebp
mov	%esp,%ebp


lea (mp),%eax
push %eax
lea (sec),%eax
push %eax
push $0xacce55ed

call practice

leave
ret


