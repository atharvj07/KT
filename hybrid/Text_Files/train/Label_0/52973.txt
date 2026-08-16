import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int heapSize = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        Node[] node = new Node[heapSize + 1];
        for(int i = 1; i <= heapSize; i++){
            node[i] = new Node(i);
            node[i].key = Integer.parseInt(input[i-1]);
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i <=heapSize; i++){
            if(2*i <= heapSize){
                node[i].left = node[2*i];
                node[2*i].parent = node[i];
            }
            if(2*i + 1 <= heapSize){
                node[i].right = node[2*i + 1];
                node[2*i + 1].parent = node[i];
            }
            sb.append("node ").append(i).append(": ");
            sb.append("key = ").append(node[i].key).append(", ");
            if(node[i].parent != null){
                sb.append("parent key = ").append(node[i].parent.key).append(", ");
            }
            if(node[i].left != null){
                sb.append("left key = ").append(node[i].left.key).append(", ");
            }
            if(node[i].right != null){
                sb.append("right key = ").append(node[i].right.key).append(", ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }

}
class Node{
    int id, key;
    Node left, right, parent;
    Node(int id){
        this.id = id;
    }
}