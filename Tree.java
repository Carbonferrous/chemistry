import java.util.*;
//count leaves
class Tree<E>
{
	private Node<E> root;
	private Node<E> branch;	
	
	public Tree()
	{
		root = new Node<E>();
		branch = root;
	}
	
	public Node<E> getBranch()
	{
		return branch;
	}
	public boolean toChild(int childIndex)
	{
		if(branch.isLeaf())
			return false;
		branch = branch.getChildAt(childIndex);
		return true;
	}
	public boolean toParent()
	{
		if(branch.getParent() == null)
			return false;
		branch = branch.getParent();
		return true;
	}
	public void toRoot()
	{
		branch = root;
	}
	public void toBranch(ArrayList<Integer> p)
	{
		for(Integer i : p)
		{
			if(!toChild(i))
				break;
		}
	}
	public void toNode(Node<E> n)
	{
		toBranch(branch.searchFor(n));
	}
}