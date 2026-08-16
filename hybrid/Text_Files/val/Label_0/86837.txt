import java.util.Scanner;

public class Codechef {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String x = input.next();
        int n = input.nextInt(), c = 0, c1 = 0;
        String[] s = new String[n];
        for (int i = 0; i < n; i++) {
            s[i] = input.next();
        }

        for (int i = 0; i < n; i++) {
            if (x.equals(s[i])) {
                System.out.println("Yes");
                c++;
                break;
            }
        }

        if (c == 0) {
            for (int i = 0; i < n; i++) {

                if (s[i].charAt(1) == x.charAt(0)) {
                    for (int j = 0; j < n; j++) {
                        if (s[j].charAt(0) == x.charAt(1)) {
                            System.out.println("Yes");
                            c++;
                            break;
                        }
                        
                    }
                    if(c==1){
                        break;
                    }

                }

            }
        }
        if (c == 0) {
            System.out.println("No");
        }

    }

}
