import java.util.Scanner;

public class SolutionPr {
    
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int t;
        t = sc.nextInt();
        
        while (t-- > 0) {
            int n, k;
            int [] arr = new int [2];
            arr[0] = sc.nextInt();
            arr[1] = sc.nextInt();
            sc.nextLine();
            String s;
            s = sc.nextLine();
            int count = 0;
            StringBuilder sbf = new StringBuilder(s);
            if (arr[0] == 1) {
                if (sbf.charAt(0) == '*') System.out.println(1);
                else System.out.println(0);
                return;
            }
            
            for (int i = 0; i < arr[0]; ++i) {
                if (sbf.charAt(i) == '*') {
                    sbf.setCharAt(i, 'x');
                    count++;
                    break;
                }
            }
            
            for (int i = arr[0] - 1; i >=0; --i) {
                if (sbf.charAt(i) == '*') {
                    sbf.setCharAt(i, 'x');
                    count++;
                    break;
                }
            }
            
            for (int i = 0; i < arr[0]; ++i) {
                if (sbf.charAt(i) == '.') continue;
                if (sbf.charAt(i) == 'x') {
                    boolean flag = false;
                    for (int j = 1; j <= arr[1]; ++j) {
                        if (i + j < arr[0] && sbf.charAt(i + j) == 'x') {
                            flag = true;
                            break;
                        } else if (i + j >= arr[0]) {
                            flag = true;
                            break;
                        }
                    }
                    
                    if (flag == false) {
                        for (int j = i + arr[1]; j > i; --j) {
                            if (j < arr[0] && sbf.charAt(j) == '*') {
                                sbf.setCharAt(j, 'x');
                                count++;
                                break;
                            }
                        }
                    }
                    
                }
            }
            //System.out.println(sbf.toString());
            System.out.println(count);
        }
    } 
}
