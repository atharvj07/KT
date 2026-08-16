import java.util.Scanner;

class Main {
    static class Calculator {
        enum Operator {
            NULL {
                @Override
                public int apply(int r1, int r2) {
                    if (r2 < 0 || r2 > 9999) {
                        throw new RuntimeException();
                    } else {
                        return r2;
                    }
                }
            },
            ADD {
                @Override
                public int apply(int r1, int r2) {
                    if (r1 + r2 < 0 || r1 + r2 > 9999) {
                        throw new RuntimeException();
                    } else {
                        return r1 + r2;
                    }
                }
            },
            SUB {
                @Override
                public int apply(int r1, int r2) {
                    if (r1 - r2 < 0 || r1 - r2 > 9999) {
                        throw new RuntimeException();
                    } else {
                        return r1 - r2;
                    }
                }
            },
            MULT {
                @Override
                public int apply(int r1, int r2) {
                    if (r1 * r2 < 0 || r1 * r2 > 9999) {
                        throw new RuntimeException();
                    } else {
                        return r1 * r2;
                    }
                }
            };
            public int apply(int r1, int r2) {
                return 0;
            }
        }

        private int calc(char[] input) {
            int R1 = 0;
            int R2 = 0;
            Operator R3 = Operator.NULL;

            for (int i = 0; input[i] != '='; i++) {
                if (Character.isDigit(input[i])) {
                    R2 = Operator.MULT.apply(R2, 10);
                    R2 = Operator.ADD.apply(R2, input[i] - '0');
                } else if (input[i] == '+') {
                    R1 = R3.apply(R1, R2);
                    R2 = 0;
                    R3 = Operator.ADD;
                } else if (input[i] == '-') {
                    R1 = R3.apply(R1, R2);
                    R2 = 0;
                    R3 = Operator.SUB;
                } else if (input[i] == '*') {
                    R1 = R3.apply(R1, R2);
                    R2 = 0;
                    R3 = Operator.MULT;
                } else {
                    assert false;
                }
            }
            R1 = R3.apply(R1, R2);
            R2 = 0;
            R3 = Operator.NULL;
            return R1;
        }

        public void run(char[] input) {
            try {
                System.out.println(calc(input));
            } catch (Throwable e) {
                System.out.println("E");
            }
        }
    }

    private static void solve() {
        Scanner scanner = new Scanner(System.in);
        Calculator calculator = new Calculator();

        while (scanner.hasNext()) {
            char[] input = scanner.next().toCharArray();
            calculator.run(input);
        }
    }

    public static void main(String... args) {
        solve();
    }
}