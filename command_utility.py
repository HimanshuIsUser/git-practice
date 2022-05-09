import argparse
import sys

# def calc(args):
#     if args.o=='add':
#         return args.x + args.y
#     elif args.o=='sub':
#         return args.x - args.y
#     elif args.o=='mul':
#         return args.x * args.y
#     elif args.o=='div':
#         return args.x / args.y
#     else:
#         print("some thing went wrong")
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,
#                         help="call himanshu - 9818812568")
#     parser.add_argument('--y',type=float,default=3.0,
#                         help="call himanshu - 9818812568")
#     parser.add_argument('--o',type=str,default="add",
#                         help="call himanshu - 9818812568")
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))

#...................................................................
def fakecal_culator(args):
    if args.x == 43 and args.y == 3 and args.o == str('*'):
        return 555
    elif args.x == 56 and args.y == 9 and args.o == str('+'):
        return 77
    elif args.x == 56 and args.y == 6 and args.o == str('/'):
        return 4
    elif args.o == str('*'):
        return args.x * args.y
    elif args.o == str('+'):
        return args.x + args.y
    elif args.o == str('/'):
        return args.x / args.y
    elif args.o == str('-'):
        return args.x - args.y1
    elif args.o == str('%'):
        return args.x % args.y
    else:
        print("error! please give correct option only")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1,
                        help="thanks for calling us,but we dont care .|.")
    parser.add_argument('--y',type=float,default=2,
                        help="thanks for calling us,but we dont care .|.")
    parser.add_argument('--o',type=str,default='+',
                        help="thanks for calling us,but we dont care .|.")
    args = parser.parse_args()
    sys.stdout.write(str(fakecal_culator(args)))

# one console panel and go to open fistfrog directry and enter this :- python command_utility.py --x 56 --y 9 --o +
# this command run this programe in console panel


