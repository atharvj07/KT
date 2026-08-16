import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// YAML
// 2012/10/29
public class Main{
	Scanner sc=new Scanner(System.in);

	String query;
	ArrayList<String> ss;

	void run(){
		query=sc.nextLine();
		ss=new ArrayList<String>();
		for(; sc.hasNextLine();){
			ss.add(sc.nextLine());
		}
		solve();
	}

	void solve(){
		Node root=new Node("", "", -1, null);
		Node node=root;
		for(String line : ss){
			int depth=line.length();
			line=line.replaceAll("^ *", "");
			depth-=line.length();
			for(; depth<=node.depth; node=node.parent);
			if(line.charAt(line.length()-1)==':'){
				Node child=new Node(line.substring(0, line.length()-1), null,
						depth, node);
				node.children.put(child.key, child);
				node=child;
			}else{
				String key=line.split(": ")[0];
				String value=line.split(": ")[1];
				Node child=new Node(key, value, depth, node);
				node.children.put(child.key, child);
			}
		}

		String ans;
		node=root;
		for(String s : query.substring(1).split("\\.")){
			if(node.children.containsKey(s)){
				node=node.children.get(s);
			}else{
				node=null;
				break;
			}
		}
		if(node==null){
			ans="no such property";
		}else if(node.children.size()>0){
			ans="object";
		}else{
			ans="string \""+node.value+"\"";
		}
		println(ans);
	}

	class Node{
		String key, value;
		int depth;
		Node parent;
		HashMap<String, Node> children;

		Node(String key, String value, int depth, Node parent){
			this.key=key;
			this.value=value;
			this.depth=depth;
			this.parent=parent;
			children=new HashMap<String, Node>();
		}
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}