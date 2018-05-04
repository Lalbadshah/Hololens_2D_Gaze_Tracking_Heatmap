using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using System.Threading;
using UnityEngine.XR.WSA;



public class HeatmapImageUpdater : MonoBehaviour {

    bool TimetoUpdate;
    Thread WorkerThread;

    public RawImage HeatmapImage;

    // Use this for initialization
    void Start () {
        Debug.Log("Entered Start Funtion");
        TimetoUpdate = false;
        WorkerThread = new Thread(new ThreadStart(Initerator));
        WorkerThread.IsBackground = true;
        WorkerThread.Start();

        //UnityEngine.XR.WSA.HolographicSettings.ReprojectionMode = HolographicSettings.HolographicReprojectionMode.Disabled;
	}

    void Initerator()
    {
        while (true)
        {
            Debug.Log("Entered Start loop");
            System.Threading.Thread.Sleep(10000); //update every 10 seconds
            TimetoUpdate = true;
        }

    }

    // Call when exit application
    private void OnApplicationQuit()
    {
        Stop();
    }

    // Stop all of process
    private void Stop()
    {
        WorkerThread.Abort();
        
    }

    // Update is called once per frame
    void Update () {
        if (TimetoUpdate)
        {
            const string V = "C:\\Users\\tgbtg\\OneDrive\\Documents\\CIIS2\\GazeModule-master\\src\\Current_Map.PNG";
            string filePath = V; 
            Texture2D tex = null;
            byte[] fileData;

            if (File.Exists(filePath))
            {
                fileData = File.ReadAllBytes(filePath);
                tex = new Texture2D(2, 2);
                tex.LoadImage(fileData); //..this will auto-resize the texture dimensions.
            }

            HeatmapImage.texture = tex;
            TimetoUpdate = false;
        }
	}
}
