import java.util.*;

class Node<E>
{
	private E data;
	private Node<E> parent;
	private ArrayList<Node<E>> children;
	
	//Constructors
	public Node()
	{
		helper(null, null);
	}
	public Node(E d)
	{
		helper(d, null);
	}
	public Node(Node<E> p)
	{
		helper(null, p);
	}
	public Node(E d, Node<E> p)
	{
		helper(d, p);
	}
	private void helper(E d, Node<E> p)
	{
		data = d;
		parent = p;
		children = new ArrayList<Node<E>>();
	}
	
	//Getters
	public E getData()
	{
		return data;
	}
	public Node<E> getParent()
	{
		return parent;
	}
	public ArrayList<Node<E>> getChildren()
	{
		return children;
	}
	public Node<E> getChildAt(int childIndex)
	{
		return children.get(childIndex);
	}
	public boolean contains(Node<E> n)
	{
		for(Node<E> c : children)
			if(c.equals(n))
				return true;
		return false;
	}
	public boolean equals(Node<E> n)
	{
		if(getChildCount() != n.getChildCount())
			return false;
		if(isLeaf())
		{
			if(data == null)
			return n.getData() == null;
			return data.equals(n.getData());
		}
		for(int x = 0; x < getChildCount(); x ++)
			if(!getChildAt(x).equals(n.getChildAt(x)))
				return false;
		return true;
	}
	public int getChildCount()
	{
		return children.size();
	}
	public int getIndexOf(Node<E> node)
	{
		for(int i = 0; i < getChildCount(); i ++)
			if(node.equals(children.get(i)))
				return i;
		return -1;
	}
	public boolean isLeaf()
	{
		return children.isEmpty();
	}
	public String toString()
	{
		if(data == null)
			return "null";
		return data.toString();
	}
	public ArrayList<E> toArrayList()
	{
		ArrayList<E> datas = new ArrayList<E>();
		datas.add(data);
		if(isLeaf())
			return datas;
		for(Node<E> e: children)
			datas.addAll(e.toArrayList());
		return datas;
	}
	public ArrayList<Integer> searchFor(Node<E> n)
	{
		ArrayList<Integer> loc = new ArrayList<Integer>();
		if(this.equals(n))
		{
			loc.add(0);
			return loc;
		}
		for(int x = 0; x < getChildCount(); x ++)
		{
			ArrayList<Integer> foo = children.get(x).searchFor(n);
			if(!foo.isEmpty())
			{
				loc.add(x);
				loc.addAll(foo);
				return loc;
			}
		}
		return loc;
	}
	//Setters
	public void setData(E d)
	{
		data = d;
	}
	public void setParent(Node<E> p)
	{
		parent = p;
		parent.addChild(this);
	}
	public void setParent(Node<E> p, int index)
	{
		parent = p;
		parent.addChild(index, this);
	}
	public void addChild(Node<E> n)
	{
		children.add(n);
	}
	public void addChild(int childIndex, Node<E> n)
	{
		children.add(childIndex, n);
	}
	public void addChild(E d)
	{
		children.add(new Node<E>(d, this));
	}
	public void addChild(int childIndex, E d)
	{
		children.add(childIndex, new Node<E>(d, this));
	}
	public void addChildren(ArrayList<Node<E>> c)
	{
		children.addAll(c);
	}
	public void setChild(int childIndex, Node<E> c)
	{
		children.set(childIndex, c);
	}
	public void setChildren(ArrayList<Node<E>> c)
	{
		children = c;
	}
	public void removeChild(int childIndex)
	{
		children.remove(childIndex);
	}
	public void removeChild(Node<E> n)
	{
		children.remove(n);
	}
	public void removeChildren(ArrayList<Node<E>> c)
	{
		children.removeAll(c);
	}
}