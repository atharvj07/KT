import java.util.Scanner;

public class Palindromic_Supersequence {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String s;
        String s1;

        boolean is;
        int i,l,l1,j;
        while (input.hasNext()){
            is=false;
            s1="";
            s = input.nextLine();
            l=s.length();
            l1=l;
            l1--;
            l/=2;
            for(i=0;i<l;i++,l1--){
                if(s.charAt(i)!=s.charAt(l1))
                {
                    is = true;
                    break;
                }
            }
            if(is==false)
                System.out.println(s);
            else {
                l1=s.length();
                l1--;
                for(i=l1,j=0;i>=0;i--,j++){
                    s1 += s.charAt(i);
                }
                System.out.println(s+s1);
            }
        }
    }
}
