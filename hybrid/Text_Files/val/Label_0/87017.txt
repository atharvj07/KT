import java.util.Scanner;


public class LittelEltBits {

    /**
     * @param args
     */
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        
        Scanner s = new Scanner(System.in);
        String a = s.next();
        int index = a.indexOf('0');
        //System.out.println(index);
        if(index==-1) System.out.println(a.substring(1));
        else
        {
            System.out.print(a.substring(0,index));
            System.out.println( a.substring(index+1));
        }

    }

}
