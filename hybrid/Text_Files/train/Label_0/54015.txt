import java.io.*;
public class Main {

    public static void main(String[] args) {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try{
            String s = br.readLine();
            int n = Integer.parseInt(br.readLine());
            s = s.toLowerCase();
            String ans = "";
            for(int i = 0; i < s.length(); ++i)
            {
                char c = s.charAt(i);
                if(c < n + 97)
                {
                  ans = ans + Character.toUpperCase(c);
                }
                else{
                    ans = ans + Character.toLowerCase(c);
                }
            }
            System.out.println(ans);
        }
        catch(Exception e){

        }
    }
}
