import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        String line=sc.nextLine();
        String ans="";
        int length=line.length();
        for(int i=0;i<length;i++){
            char ch=line.charAt(i);
            if(Character.isLowerCase(ch)){
                ans+=Character.toUpperCase(ch);

            }
            else ans+=Character.toLowerCase(ch);
        }
        System.out.println(ans);
    }
}
