import java.util.Scanner;

public class A {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        String s = scn.next();
        boolean flag = false;
        
        if(s.charAt(0) == '?' || s.contains("??") || s.charAt(n - 1) == '?') 
            flag = true;
        
        for (int i = 0; i < n -1; i++) {
            
            if(s.charAt(i) != '?' && s.charAt(i) == s.charAt(i+1)) {
                flag = false;
                break;
            }
            if(i != 0 && s.charAt(i) == '?' && s.charAt(i-1) == s.charAt(i+1) && 
                    s.charAt(i-1) != '?' && s.charAt(i+1) != '?') {
                flag = true;
                break;
            }
        }
        
        if(flag)
            System.out.println("Yes");
        else
            System.out.println("No");
        
    }
}
