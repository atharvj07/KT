import java.util.Scanner;


public class GiveString23A {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String stroke = in.next();
        char[] s = new char [stroke.length()];
        for (int i=0;i<stroke.length();i++)
            s[i]=stroke.charAt(i);
        int dlina = 0;
        for (int i=0;i<s.length-1;i++)
            for (int j=i+1;j<s.length;j++)
                for (int k=0;k<(s.length-j);k++)
                    if (s[i]==s[j])
                    {
                        int ik=i+k;
                        int jk = j+k;
                        if (s[ik]==s[jk])
                        {
                            if (dlina<k+1)
                                dlina=k+1;      
                        }
                        else 
                        break;
                    }       
        System.out.println(dlina);
    }
}
