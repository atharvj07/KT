import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class TaskE {
    public static void main(String[] args) {
        InputStream inputStream;
        String str = null;
        if(str == null){
            inputStream = System.in;
        }else{
            inputStream = new ByteArrayInputStream(str.getBytes());
        }
        
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Solver solver = new Solver();
        solver.solve(1, in, out);
        out.close();
    }
    

    static class Solver {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int numPeople = in.nextInt();
            Person[] people = new Person[numPeople+1];
            
            HashMap<Integer, ArrayList<Integer>> levels = new HashMap<>();
            LinkedList<Person> roots = new LinkedList<>();
            
            
            for(int i=1;i<=numPeople;i++){
                people[i] = new Person();
                people[i].index = i;
            }
            
            for(int i=1;i<=numPeople;i++){
                people[i].parent = people[in.nextInt()];
                //if(people[i].parent != null)
                //System.out.println("Node " + i + " has parent " + people[i].parent.index);
                if(people[i].parent == null){
                    roots.add(people[i]);
                }else{
                    people[i].parent.children.add(people[i]);
                }
            }
            
            //preprocess
            int counter = 1;
            HashMap<Integer, Person> origIDtoNewID  = new HashMap<>();
            for(Person root : roots){
                LinkedList<Person> toVisit = new LinkedList<>();
                HashSet<Person> visited = new HashSet<>();
                toVisit.add(root);
                //System.out.println("Starting");
                while(!toVisit.isEmpty()){
                    
                    Person current = toVisit.getFirst();
                    if(visited.contains(current)){
                        if(current.children.isEmpty()){
                            toVisit.remove(current);
                            if(current.parent!=null){
                                current.parent.maxChild = Math.max(current.ID, current.maxChild);
                                //System.out.println(current.index+" " + current.parent.maxChild);
                            }
                        }else{
                            toVisit.addFirst(current.children.removeFirst());
                        }
                    }else{
                        current.ID = counter++;
                        current.maxChild = current.ID;
                        origIDtoNewID.put(current.ID, current);
                        //System.out.println("Mapping: " + current.index + " to "+ current.ID);
                        visited.add(current);
                        if(current.parent != null){
                            current.height = current.parent.height+1;
                        }
                        if(!levels.containsKey(current.height)){
                            levels.put(current.height, new ArrayList<>());
                        }
                        levels.get(current.height).add(current.ID);
                    }
                }
            }
            
            int numQueries = in.nextInt();
            
            StringBuilder answers = new StringBuilder();
            for(int query=0;query<numQueries;query++){
                Person target = people[in.nextInt()];
                int level = in.nextInt();
                
                //System.out.println(query+": looking at node " + target.index + " parent is " + (target.parent == null ? null : target.parent.index));
                if(level > target.height){
                    answers.append(0+" ");
                    continue;
                }
                
                //System.out.println("Searching: " + target.ID);
                int parentIndex = levels.get(target.height-level).get((Collections.binarySearch(levels.get(target.height-level), target.ID)+1)*-1-1);
                //System.out.println(levels.get(target.height-level));
                //System.out.println(parentIndex+" is parent");
                Person parent = people[origIDtoNewID.get(parentIndex).index];
                
                int left = parent.ID;
                int right = parent.maxChild+1;
                
                int l = Collections.binarySearch(levels.get(target.height), left);
                int r = Collections.binarySearch(levels.get(target.height), right);
                //System.out.println(left + " "+ right + " -> " + l + " " +r + " " + levels.get(target.height));
                
                if(l < 0){
                    l = (l+1)*-1;
                }
                if(r < 0){
                    r = (r+1)*-1;
                }
                //System.out.println(left + " "+ right + " -> " + l + " " +r);
                //System.out.println();
                answers.append(r-l-1);
                answers.append(" ");
            }
            
            System.out.println(answers);
        }
    }
    
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
 
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
 
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
 
        public int nextInt() {
            return Integer.parseInt(next());
        }
        
        public long nextLong() {
            return Long.parseLong(next());
        }
    }
}

class Person{
    Person parent;
    LinkedList<Person> children = new LinkedList<>();
    int ID;
    int index;
    int height = 0;
    int maxChild = 0;
}