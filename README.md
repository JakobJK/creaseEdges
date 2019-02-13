# creaseEdges

creaseEdges is a set of commands created for Autodesk Maya to help how you work with creased edges.

---
## Setup

Put the creaseEdges.py file in your maya scripts directory and restart/rehash maya.
You can now import it as any other python module inside of Maya.

## Usage

For now, the creaseEdges script has three commands.

* setCrease - set the crease value of selected edges
* selectCrease - select the edges of matching crease value.
* clearCrease - clear any crease on your selected meshes.

The following example sets the selected edges to a crease value of 3:

```python
import creaseEdges

creaseEdges.setCrease(3)
```

The following example selects edges with a specific crease value. Note: if no crease value is set in the paranthesis, all edges that has any creasing at all will be selected.

```python
import creaseEdges

creaseEdges.selectCrease()
```

The last example clear any creasing on your selected objects.

```python
import creaseEdges

creaseEdges.clearCrease()
```

## Author

[**Jakob Kousholt**](https://www.linkedin.com/in/jakejk/) - Freelance Creature Modeller

## License

creaseEdges is licensed under the [MIT](https://rem.mit-license.org/) License.