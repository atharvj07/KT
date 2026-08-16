import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;
import java.io.*;
//import java.util.stream.IntStream;



class Node{
    static int INFTY = Integer.MAX_VALUE;

    int id;
    int d = INFTY;   // startからの距離(更新する)
    //int parent;
    //int color = 1;
    Map<Integer, Integer> children = new TreeMap<>(); // <id, distance>

    Node(){};

    Node(int id){
        this.id = id;
    }

}

public class Main {
    static int INFTY = Integer.MAX_VALUE;

    static Node[] nodes;
    //static int[] d;         // startからの最短距離
    //static Set<Integer> T;  // 全域木
    //static Set<Integer> V;  // 探索前

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = sc.nextInt();
            nodes = new Node[n];
            //d = new int[n];
            //Arrays.fill(d, INFTY);

            for(int i=0;i<n;i++){
                int id = sc.nextInt();
                int numChild = sc.nextInt();
                nodes[i] = new Node(id);
                for(int j=0;j<numChild;j++){
                    int child = sc.nextInt();
                    int weight = sc.nextInt();
                    nodes[id].children.put(child, weight);
                }
            }

            Queue<Node> queue = new PriorityQueue<>((o1,o2)->{return o1.d-o2.d;});  // 全域木からの距離でソート
            
            queue.add(nodes[0]);
            //nodes[0].color = 1;
            nodes[0].d = 0;
            while(!queue.isEmpty()){
                Node u = queue.poll();
                //if(u.cost + d[u.parent] > d[u.id]){continue;}
                

                for(Map.Entry<Integer, Integer> entry : u.children.entrySet()){
                    int id = entry.getKey();
                    int cost = entry.getValue();
                    if(nodes[id].d < nodes[u.id].d + cost){continue;}

                    nodes[id].d = nodes[u.id].d + cost;
                    //nodes[id].color = 1;
                    queue.add(nodes[id]);
                }
                
            }
            
            StringBuffer buf = new StringBuffer();
            for(int i=0;i<n;i++){
                buf.append(i + " " + nodes[i].d + '\n');
            }
            System.out.print(buf);
        
    }



}



