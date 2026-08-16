import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.Scanner;
 
public class Main {
     
    public static class WeightUnionFind{
        int[] parent;
        int[] rank;
        int[] diff_weight;
         
        WeightUnionFind(int n){
            parent=new int[n];
            rank = new int[n];
            diff_weight = new int[n];
             
            for(int i=0;i<n;i++){
                parent[i]=i;
                rank[i] = 0;
                diff_weight[i] = 0;
            }
        }
         
        public int find(int x){
            if(parent[x]==x){
                return x;
            }
             
            return find(parent[x]);
        }
         
        public int find_diff(int x){
            if(parent[x] == x){
                return 0;
            }
             
            return find_diff(parent[x]) + diff_weight[x];
        }
         
        public Boolean same(int x,int y){
            return find(x)==find(y);
        }
         
        public int get_diff(int x, int y){
            if(!same(x, y)){
                return Integer.MIN_VALUE;
            }else{
                return find_diff(x) - find_diff(y);
            }
        }
        /*
        public void unite(int x,int y){
            x = find(x);
            y = find(y);
             
            if(x == y){
                return;
            }
             
            if(rank[x] < rank[y]){
                parent[x] = y;
            }else{
                parent[y] = x;
                if(rank[x] == rank[y]){
                    rank[x]++;
                }
            }
        }
        */
        public void set_diff(int x,int y, int d){
            final int find_x = find(x);
            final int find_y = find(y);
             
            if(find_x == find_y){
                return;
            }
             
            //System.out.println(x + " " + find_x + " " + y + " " + find_y + " " + diff_weight[y] + " " + diff_weight[x]);
            d -= find_diff(x) - find_diff(y);
             
            if(rank[find_x] < rank[find_y]){
                //diff_weight[x] += d + find_diff(y);
                diff_weight[find_x] = d;
                 
                parent[find_x] = find_y;
            }else{
                diff_weight[find_y] = -d;
                 
                parent[find_y] = find_x;
                if(rank[find_x] == rank[find_y]){
                    rank[find_x]++;
                }
            }
        }
    }
 
     
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         
        while (true) {
            final int N = sc.nextInt();
            final int M = sc.nextInt();
 
            if (N == 0 && M == 0) {
                break;
            }
             
            System.gc();
             
            WeightUnionFind wuf = new WeightUnionFind(N);
             
            for(int i = 0; i < M; i++){
                String op = sc.next();
                 
                if(op.equals("!")){
                    final int from = sc.nextInt() - 1;
                    final int to = sc.nextInt() - 1;
                    final int w = sc.nextInt();
                     
                    wuf.set_diff(from, to, w);
                    //System.out.println("DIFF " + from + " " + to + " " + w);
                }else{
                    final int from = sc.nextInt() - 1;
                    final int to = sc.nextInt() - 1;
                     
                    if(!wuf.same(from, to)){
                        System.out.println("UNKNOWN");
                    }else{
                        System.out.println(wuf.get_diff(from, to));
                    }
                }
                 
                //System.out.println("P : " + Arrays.toString(wuf.parent));
                //System.out.println("D : " + Arrays.toString(wuf.diff_weight));
            }
             
        }
 
        sc.close();
    }
 
}