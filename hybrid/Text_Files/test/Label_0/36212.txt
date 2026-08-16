import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class CF_A_1384
{
    public static void main(String[] args) throws IOException
    {
        int t = readInt();
        for (int __ = 0; __ < t; __++)
        {
            int n = readInt();
            StringBuilder lastStr = new StringBuilder("a".repeat(200));
            System.out.println(lastStr);
            for (int i = 0; i < n; i++)
            {
                int a = readInt();
                StringBuilder curStr = new StringBuilder(lastStr);

                char separateChr = curStr.charAt(a);
                if (separateChr - 'a' >= 23)
                {
                    separateChr--;
                }
                else
                {
                    separateChr++;
                }
                curStr.setCharAt(a, separateChr);
                System.out.println(curStr);
                lastStr = curStr;
            }
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int readInt() throws IOException
    {
        while (st == null || !st.hasMoreTokens())
        {
            st = new StringTokenizer(br.readLine());
        }
        return Integer.parseInt(st.nextToken());
    }
}
