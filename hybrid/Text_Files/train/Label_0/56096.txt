import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.TreeSet;


public class vk18
{
    public static void main(String[] stp) throws Exception
    {
        Scanner scan = new Scanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken()),i;
        Integer count[]=new Integer[n+1];
        boolean flag[]=new boolean[n+1];
        Arrays.fill(count,0);
        Arrays.fill(flag,false);
        st = new StringTokenizer(br.readLine());
        Integer input[]=new Integer[n];
        for(i=0;i<n;i++)
        {
            input[i]=Integer.parseInt(st.nextToken());
            count[input[i]]++;
        }
        TreeSet<Integer> ts=new TreeSet<>();
        for(i=1;i<n+1;i++) if(count[i]==0) ts.add(i);
        int ans=ts.size();
        i=0;
        while(ts.size()!=0)
        {
            int ele=ts.pollFirst();
            for(;i<n;i++)
            {
                if(flag[input[i]]==false && count[input[i]]==1) { flag[input[i]]=true; count[input[i]]--;  }
                else if(flag[input[i]]==false && count[input[i]] > 1)
                {
                    if(ele < input[i])
                    {
                        count[input[i]]--;
                        input[i]=ele;
                        break;
                    }
                    else
                    {
                        flag[input[i]]=true; count[input[i]]--;
                    }
                }
                else if(flag[input[i]]==true && count[input[i]] >= 1)
                {
                    count[input[i]]--;
                    input[i]=ele;
                     break;
                }
            }
        }
        pw.println(ans);
        for(i=0;i<n;i++) pw.print(input[i]+" ");
        pw.flush();
    }
}