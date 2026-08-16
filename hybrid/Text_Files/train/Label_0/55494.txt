import java.util.Scanner;

public class Main{

    /**
     * @param args
     */
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N = sc.nextInt();   
        while(N-->0){
            String s = sc.next();
            String t = sc.next();
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(s.length()-i-1);
                switch(c){
                case 'J':
                    t=J(t);
                    break;
                case 'C':
                    t=C(t);
                    break;
                case 'E':
                    t=E(t);
                    break;
                case 'A':
                    t=A(t);
                    break;
                    
                case 'P':
                    t=P(t);
                    break;
                case 'M':
                    t=M(t);
                    break;
                }
            }
            System.out.println(t);
        }
    }

    private static String M(String t) {
        char[] s = t.toCharArray();
        for (int i = 0; i < s.length; i++) {
            if(Character.isDigit(s[i])){
                s[i]++;
                if(s[i]=='9'+1){
                    s[i]='0';
                }
            }
        }
        return new String(s);
    }

    private static String P(String t) {
        char[] s = t.toCharArray();
        for (int i = 0; i < s.length; i++) {
            if(Character.isDigit(s[i])){
                s[i]--;
                if(s[i]=='0'-1){
                    s[i]='9';
                }
            }
        }
        return new String(s);
    }

    private static String A(String t) {
        return new StringBuffer(t).reverse().toString();
    }

    private static String E(String t) {
        if(t.length()%2==0){
            return t.substring(t.length()/2)+t.substring(0,t.length()/2);
        }
        return t.substring(t.length()/2+1)+t.charAt(t.length()/2)+t.substring(0,t.length()/2);
    }

    private static String C(String t) {
        char[] s = new char[t.length()];
        for (int i = 1; i < t.length(); i++) {
            s[i-1]=t.charAt(i);
        }
        s[s.length-1]=t.charAt(0);
        return new String(s);
    }

    private static String J(String t) {
        char[] s = new char[t.length()];
        for (int i = 0; i < t.length()-1; i++) {
            s[i+1]=t.charAt(i);
        }
        s[0]=t.charAt(t.length()-1);
        return new String(s);
    }

}