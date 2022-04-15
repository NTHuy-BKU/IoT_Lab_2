using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Manage : MonoBehaviour
{
    public Text _test;
     public InputField input_broker;
     public InputField input_usename;
     public InputField input_Pass;

    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("hello");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void Display()
    {
      if (input_usename.text == "bkiot" && input_Pass.text == "12345678"){
          SceneManager.LoadScene("Scene2");
      }
      else{
          _test.text = "Username or Passwork is incorrect";
      }
    }
}
