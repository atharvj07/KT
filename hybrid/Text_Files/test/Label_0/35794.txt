import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.Collections;
//import java.util.Iterator;
//import java.util.LinkedList;
//import java.util.List;
//import java.util.Vector;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] tmpArray = br.readLine().split(" ");
		int n = Integer.parseInt(tmpArray[0]);
		int q = Integer.parseInt(tmpArray[1]);

//		@SuppressWarnings("unchecked")
//		ArrayList<Integer>[] listArray = new ArrayList[n];
		
		MyList[] lists = new MyList[n];
		for(int i = 0; i < n; i++){
//			listArray[i] = new ArrayList<Integer>();
//			listArray[i] = new LinkedList<Integer>();
			
			lists[i] = new MyList();
		}

		for(int i = 0; i < q; i++){
//			System.out.println("query: "+i);
			tmpArray = br.readLine().split(" ");

			//insert
			if(tmpArray[0].equals("0")){
				int t = Integer.parseInt(tmpArray[1]);
				int x = Integer.parseInt(tmpArray[2]);

//				listArray[t].add(x);
//				Collections.addAll(listArray[t], x);
//				print(vecArray[t]);
//				System.out.println("========");
				lists[t].add(x);
			}
			//dump
			else if(tmpArray[0].equals("1")){
				int t = Integer.parseInt(tmpArray[1]);

//				printList(listArray[t]);
//				printList(listArray[t]);
				lists[t].dump();
			}
			//splice
			else {

				int s = Integer.parseInt(tmpArray[1]);
				int t = Integer.parseInt(tmpArray[2]);
				if(true){
					lists[t].splice(lists[s]);
					continue;
				}
				
//				if(!listArray[s].isEmpty()){
////					if(listArray[t].size() > 0){
//					if(true){
//						Integer[] va = listArray[s].toArray(new Integer[0]);
//						//					Integer[] vb = listArray[t].toArray(new Integer[0]);
//						//					
//						//					Integer vc[] = new Integer[va.length + vb.length];
//						//					System.arraycopy(vb, 0, vc, 0, vb.length);
//						//					System.arraycopy(va, 0, vc, vb.length, va.length);
//						//					
//						//					listArray[s] = new Vector<>();
//						//					listArray[t] = new Vector(Arrays.asList(vc));
//
//						//					listArray[t].addAll(listArray[s]);
//						Collections.addAll(listArray[t], va);
//					}
//					else {
//						listArray[t] = (ArrayList<Integer>) listArray[s].clone();
//					}
////					listArray[s] = new ArrayList<Integer>();
//					listArray[s].clear();
//					
////					for(int j = 0; j < vecArray[s].size(); j++){
////						vecArray[t].add(vecArray[s].get(j));
////					}
////					
////					vecArray[s] = new Vector<Vector>();
//				}
			}
		}

	}
	
//	static void print(Vector<Vector> vec){
//		boolean first = true;
//		
//		StringBuffer sb = new StringBuffer();
//		
//		for(int i = 0; i < vec.size(); i++){
////			System.out.println("size = "+vec.size());
//			Vector tmpVec = vec.get(i);
//			for(int j = 0; j < tmpVec.size() ; j++){
//				if(!first){
//					sb.append(" ");
//				}
//				
//				sb.append(tmpVec.get(j));
//
//				first = false;
//			}
//		}
//		
//		System.out.println(sb);
//	}
	
//	static void printList(List list){
//        Iterator it = list.iterator();
// 
//        StringBuffer sb = new StringBuffer();
//        while(it.hasNext()){
//            sb.append(it.next());
// 
//            if(it.hasNext()){
//                sb.append(" ");
//            }
//        }
//        System.out.println(sb);
//    }
}

class MyList {
	MyNode head;
	MyNode tail;
	
	MyList (){
		head = new MyNode(0, null, null);
		tail = new MyNode(0, head, null);
		head.next = tail;
	}
	
	void add(int data){
		MyNode node = new MyNode(data, null, tail);
		
		node.prev = tail.prev;
		tail.prev = node;
		node.prev.next = node;
	}
	
	void dump(){
		MyNode current = head.next;
		
		StringBuffer sb = new StringBuffer();
		while(current.next != null){
			sb.append(current.data);
//			System.out.println("test "+current.data);
			if(current.next != tail){
				sb.append(" ");
			}
			
			current = current.next;
		}
		
		System.out.println(sb);
	}
	
	void splice(MyList list){
		MyNode first = list.head.next;
		MyNode last = list.tail.prev;
		
		first.prev = this.tail.prev;
		this.tail.prev.next = first;
		last.next = this.tail;
		this.tail.prev = last;
		
		list.head.next = list.tail;
		list.tail.prev = list.head;
	}
}

class MyNode {
	MyNode prev;
	MyNode next;
	int data;
	
	MyNode (int data, MyNode prev, MyNode next){
		this.data = data;
		this.prev = prev;
		this.next = next;
	}
}
