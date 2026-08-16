import static java.lang.Math.* ;
import static java.util.Arrays.* ;

import java.util.*;
import java.io.*;

public class Main
{
    void main() throws Exception
    {
        Scanner sc = new Scanner(System.in) ;
        PrintWriter out = new PrintWriter(System.out) ;
        char [][] s = new char[2][] ;
        s[0] = sc.next().toCharArray() ;
        s[1] = sc.next().toCharArray() ;
        if(s[0].length > s[1].length)
        {
            char [] temp = s[0] ;
            s[0] = s[1] ;
            s[1] = temp ;
        }
        int n = s[0].length ;
        SuffixAutomaton s1 = new SuffixAutomaton(s[0]) ;
        SuffixAutomaton s2 = new SuffixAutomaton(s[1]) ;

        int ans = 1 << 30 ;

        for(int l = 0 ; l < n ; l++)
        {
            int state1 = 0 ;
            int state2 = 0 ;
            for(int r = l ; r < n ; r++)
            {
                if(s1.next[state1].containsKey(s[0][r]) && s2.next[state2].containsKey(s[0][r]))
                {
                    state1 = s1.next[state1].get(s[0][r]) ;
                    state2 = s2.next[state2].get(s[0][r]) ;
                    if(s1.cnt[state1] == 1 && s2.cnt[state2] == 1)
                        ans = min(ans , r - l + 1) ;
                }
                else
                    break;
            }
        }
        if(ans == 1 << 30)
            out.println(-1);
        else
            out.println(ans);

        out.flush();
        out.close();
    }
    class SuffixAutomaton
    {
        TreeMap<Character , Integer> next[];
        int [] link , len , cnt;
        int idx , last ;
        SuffixAutomaton(char [] s)
        {
            int n = s.length ;
            link = new int [n << 1] ;
            len = new  int [n << 1] ;
            cnt = new int [n << 1] ;
            fill(cnt , 1);
            next = new TreeMap[n << 1] ;
            next[0] = new TreeMap<>() ;
            for(char c : s)
                addLetter(c) ;
            Integer [] id = new Integer[n << 1] ;
            for(int i = 0 ; i < n << 1 ; i++)
                id[i] = i ;
            sort(id , (x , y)-> len[y] - len[x]);
            for(int v : id)
                cnt[link[v]] += cnt[v]  ;
        }
        void addLetter(char c)
        {
            int curr = ++idx , p = last ;
            len[curr] = len[last] + 1 ;
            while (!next[p].containsKey(c))
            {
                next[p].put(c , curr);
                p = link[p] ;
            }

            int q = next[p].get(c) ;
            if(q != curr)
            {
                if(len[q] == len[p] + 1)
                    link[curr] = q ;
                else
                {
                    int clone = ++idx ;
                    next[clone] = (TreeMap<Character, Integer>) next[q].clone();
                    len[clone] = len[p] + 1 ;
                    link[clone] = link[q] ;
                    link[q] = link[curr] = clone ;
                    while(next[p].get(c) == q)
                    {
                        next[p].put(c , clone) ;
                        p = link[p] ;
                    }
                }
            }
            next[last = curr] = new TreeMap<>() ;
        }
    }
    class Scanner
    {
        BufferedReader br;
        StringTokenizer st;

        Scanner(InputStream in)
        {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        Scanner(String path) throws Exception
        {
            br = new BufferedReader(new FileReader(path)) ;
        }
        String next() throws Exception
        {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        int nextInt() throws Exception { return Integer.parseInt(next()); }

        long nextLong() throws Exception { return Long.parseLong(next()); }

        double nextDouble() throws Exception { return Double.parseDouble(next());}
    }

    public static void main (String [] args) throws Exception {(new Main()).main();}

}