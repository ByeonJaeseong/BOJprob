def execute_program(memory):
    acc = 0  # 가산기 (Accumulator)
    pc = 0   # 프로그램 카운터 (Program Counter)

    while True:
        instruction = memory[pc]
        pc = (pc + 1) % 32  # 다음 명령어를 가리키기 위해 PC 증가, 32바이트 메모리에서 순환

        opcode = (instruction >> 5) & 0b111  # 상위 3비트를 추출하여 명령어 종류 확인
        operand = instruction & 0b11111      # 하위 5비트를 추출하여 피연산자 확인

        if opcode == 0b000:
            memory[operand] = acc
        elif opcode == 0b001:
            acc = memory[operand]
        elif opcode == 0b010:
            if acc == 0:
                pc = operand
        elif opcode == 0b011:
            pass  # NOP 명령어
        elif opcode == 0b100:
            acc = (acc - 1) % 256  # 8비트 가산기, 감소 후 256으로 모듈러 연산
        elif opcode == 0b101:
            acc = (acc + 1) % 256  # 8비트 가산기, 증가 후 256으로 모듈러 연산
        elif opcode == 0b110:
            pc = operand
        elif opcode == 0b111:
            break  # HLT 명령어, 프로그램 종료

    return acc

import sys
input = sys.stdin.read

data = input().strip().split()
while data:
    memory = [int(data[i], 2) for i in range(32)]
    result = execute_program(memory)
    print(format(result, '08b'))
    if len(data) > 32:
        data = data[32:]
    else:
        break
