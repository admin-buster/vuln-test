from subprocess import check_output

def run(cmd:str):
  return check_output(cmd,shell=True)


if __name__ == '__main__':
  run(input('Enter number: '))
