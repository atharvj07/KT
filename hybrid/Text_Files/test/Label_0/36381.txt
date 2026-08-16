import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Node root = null;
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
		    String type = sc.next();
		    if (type.equals("insert")) {
		        if (root == null) {
		            root = new Node(sc.nextInt());
		        } else {
		            insert(sc.nextInt(), root);
		        }
		    } else if (type.equals("find")) {
		        if (find(sc.nextInt(), root)) {
		            sb.append("yes").append("\n");
		        } else {
		            sb.append("no").append("\n");
		        }
		    } else {
		        ArrayList<Integer> inList = new ArrayList<>();
		        ArrayList<Integer> preList = new  ArrayList<>();
		        get(root, inList, preList);
		        for (int x : inList) {
		            sb.append(" ").append(x);
		        }
		        sb.append("\n");
		        for (int x : preList) {
		            sb.append(" ").append(x);
		        }
		        sb.append("\n");
		    }
		}
		System.out.print(sb);
	}
	
	static class Node {
	    int key;
	    Node left;
	    Node right;
	    
	    public Node(int key) {
	        this.key = key;
	    }
	}
	
	static boolean find(int key, Node x) {
	    if (x == null) {
	        return false;
	    }
	    if (x.key == key) {
	        return true;
	    } else if (x.key > key) {
	        return find(key, x.left);
	    } else {
	        return find(key, x.right);
	    }
	}
	
	static void get(Node x, ArrayList<Integer> inList, ArrayList<Integer> preList) {
	    preList.add(x.key);
	    if (x.left != null) {
	        get(x.left, inList, preList);
	    }
	    inList.add(x.key);
	    if (x.right != null) {
	        get(x.right, inList, preList);
	    }
	}
	
	static void insert(int key, Node x) {
	    if (x.key > key) {
	        if (x.left == null) {
	            x.left = new Node(key);
	        } else {
	            insert(key, x.left);
	        }
	    } else {
	        if (x.right == null) {
	            x.right = new Node(key);
	        } else {
	            insert(key, x.right);
	        }
	    }
	}
}

