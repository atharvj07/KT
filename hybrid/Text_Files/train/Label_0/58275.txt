import java.util.Scanner;
public class solving {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int A = 0 , C = 0, G = 0, T = 0, sum = n/4;
        String s = input.next();
        char [] c = s.toCharArray();
        if(n % 4 != 0)
            System.out.println("===");
        else{
            for(int i = 0; i < c.length; i++){
                if(c[i] == 'A')
                    A++;
                if(c[i] == 'C')
                    C++;
                if(c[i] == 'G')
                    G++;
                if(c[i] == 'T')
                    T++;
            }
            if(A > sum || C > sum || G > sum || T > sum)
                System.out.println("===");
            else{
                for(int j = 0; j < c.length; j++){
                    if(c[j] == '?'){
                        if(A < sum){
                            c[j] = 'A';
                            A++;
                    }
                      else if(C < sum){
                           c[j] = 'C';
                           C++;
                    }
                      else if(G < sum){
                           c[j] = 'G';
                           G++;
                    }
                      else if(T < sum){
                          c[j] = 'T';
                           T++;
                    }
                    }
                }
                   System.out.println(c);

            }
        }
                                    
  }        
}