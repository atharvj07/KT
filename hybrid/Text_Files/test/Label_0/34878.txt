import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static Node[] nodes;
    public static void main (String[] args) throws IOException{
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int n = Integer.parseInt(br.readLine());
	nodes = new Node[n];
	for (int i = 0; i < n; i++) {
	    nodes[i] = new Node(i);
	}
	
	String[] input;
	int id, k, childId;
	int[] a;
	for (int i = 0; i < n; i++) {
	    input = br.readLine().split(" ");
	    id = Integer.parseInt(input[0]);
	    k = Integer.parseInt(input[1]);
	    nodes[id].k = k;
	    if (k == 0) {
		nodes[id].type = 1;
	    } else {
		a = new int[k];
		for (int j = 0; j < k; j++) {
		    childId = Integer.parseInt(input[2+j]);
		    a[j] = childId;
		    nodes[childId].parent = id;
		}
		nodes[id].c = a;
	    }
	}

	for (int i = 0; i < n; i++) {
	    nodes[i].depth = setDepth(i);
	}
	
	StringBuilder sb = new StringBuilder();

	for (int i = 0; i < n; i++) {
	    sb.append("node " + i);
	    sb.append(": parent = " + nodes[i].parent);
	    sb.append(", depth = " + nodes[i].depth);
	    sb.append(", ");
	    if (nodes[i].type == -1) {
		sb.append("root, ");
	    } else if (nodes[i].type == 0) {
		sb.append("internal node, ");
	    } else if (nodes[i].type == 1) {
		sb.append("leaf, ");
	    }
	    sb.append("[");
	    if (nodes[i].k != 0) {
		sb.append(nodes[i].c[0]);
	    }
	    for (int j = 1; j < nodes[i].k; j++) {
		sb.append(", " + nodes[i].c[j]);
	    }
	    sb.append("]\n");
	}
	System.out.print(sb);

    }
    public static int setDepth (int id) {
	if (nodes[id].depth >= 0) return nodes[id].depth;
	if (nodes[id].parent == -1) {
	    nodes[id].type = -1;
	    return nodes[id].depth = 0;
	}
	return nodes[id].depth = setDepth(nodes[id].parent)+1;
    }
    
}

class Node {
    int id;
    int parent;
    int depth;
    int type; //-1: root, 0: internal node, 1: leaf
    int k;
    int[] c;
    Node (int id) {
	this.id = id;
	this.parent = -1;
	this.depth = -1;
	this.type = 0;
    }
}