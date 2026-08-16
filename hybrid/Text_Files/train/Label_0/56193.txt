//created by Whiplash99
import java.io.*;
import java.util.*;
public class G
{
    private static int white=0,black=0;
    private static ArrayList<Integer> edge[];
    private static void DFS(int u, int p, int prev)
    {
        if(prev==0) black++;
        else white++;
        for(int v:edge[u])
        {
            if(v==p) continue;
            DFS(v,u,prev^1);
        }
    }
    public static void main(String[] args) throws IOException
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int i,N;

        N=Integer.parseInt(br.readLine().trim());
        edge=new ArrayList[N];
        for(i=0;i<N;i++) edge[i]=new ArrayList<>();

        for(i=0;i<N-1;i++)
        {
            String s[]=br.readLine().trim().split(" ");
            int u=Integer.parseInt(s[0])-1;
            int v=Integer.parseInt(s[1])-1;

            edge[u].add(v);
            edge[v].add(u);
        }
        
        DFS(0,0,1);
        System.out.println(Math.min(white,black)-1);
    }
}