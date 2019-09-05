.section .data
file_to_run:
.string       "/bin/sh"

.section .text
.globl _main


_main:
pushl %ebp
movl %esp, %ebp

movl $11, %eax                      
movl $file_to_run, %ebx                   
movl $0, %ecx                       
movl $0, %edx                      
int  $0x80              

leave
ret
