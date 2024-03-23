import React, { useRef, useCallback, useState } from "react";
import "./App.css";
import { IoColorFilter } from "react-icons/io5";
import { ImBrightnessContrast } from "react-icons/im";
import { IoPersonAddSharp } from "react-icons/io5";
import { RiDeleteBin5Fill } from "react-icons/ri";
import { BsCameraVideoFill } from "react-icons/bs";
import { GiNextButton } from "react-icons/gi";
import { GiPreviousButton } from "react-icons/gi";
import { IoSend } from "react-icons/io5";
import Webcam from "react-webcam";
import { v4 as uuidv4 } from "uuid";
import axios from "axios";
import Header from "./Header";

function App() {
  const [capturedImage, setCapturedImage] = useState(null);
  const [selectedImage, setSelectedImages] = useState(null);
  const [textInput, setTextInput] = useState("");
  console.log(capturedImage);
  console.log("SELECTED IMAGE====>>>>>", selectedImage);
  const uuid = uuidv4();
  const webcamReference = useRef(null);

  const handleText = (event) => {
    setTextInput(event.target.value);
  };
  console.log(textInput);

  const capture = useCallback(() => {
    const imageSrc = webcamReference.current.getScreenshot();
    setCapturedImage(imageSrc);
    setCaptured(true);
  }, [webcamReference]);

  const fetchItems = async () => {
    console.log("image returned");
    try {
      const response = await axios.get(
        `http://16.16.173.163:8000/get-url/${uuid}/1`
      );
      setSelectedImages(response.data);
    } catch (error) {
      console.error("Error fetching items:", error);
    }
  };

  const convertToBase64 = (imageSrc) => {
    return new Promise((resolve, reject) => {
      if (typeof imageSrc === "string") {
        // Handle if imageSrc is a base64 string
        resolve(imageSrc);
      } else {
        const reader = new FileReader();
        reader.readAsDataURL(imageSrc);
        reader.onload = () => resolve(reader.result.split(",")[1]);
        reader.onerror = (error) => reject(error);
      }
    });
  };

  const sendDataToBackend = async () => {
    const base64Image = await convertToBase64(capturedImage);
    const inputData = {
      user_id: uuid,
      // image_url: capturedImage,
      image_url: base64Image,
      // image_url:
      //   "https://glamourizz.s3.eu-north-1.amazonaws.com/charactor/musk.webp",
      prompt: textInput,
      gender: "male",
    };
    console.log("INPUT DATA", inputData);
    try {
      const response = await axios.post(
        "http://16.16.173.163:8000/post-prompt",

        inputData,

        {
          headers: {
            // Add your headers here
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": true,
          },
        }
      );
      console.log("Image uploaded successfully:", response.data);
      fetchItems();
    } catch (error) {
      console.error("Error uploading image:", error);
    }
  };

  return (
    <div className="app_container">
      <div className="app_wrapper">
        <Header/>

        <div className="app_image_option_wrapper">
          <div className="app_left_icons">
            <div className="app_icon app_left_icon_1">
              <IoColorFilter size={30} />
            </div>
            <div className="app_icon app_left_icon_1">
              <ImBrightnessContrast size={30} />
            </div>
            <div
              className="app_icon app_left_icon_1"
              onClick={() => capturedImage && sendDataToBackend()}
            >
              <IoSend size={30} />
            </div>
          </div>
          <div className="app_image">
            {selectedImage ? (
              <div className="captured_image">
                <div className="captured_inner_image">
                  {selectedImage && (
                    <div className="taken_picture">
                      <img
                        src={selectedImage.image_url}
                        alt="Selected"
                        style={{ maxWidth: "100%" }}
                      />
                    </div>
                  )}
                </div>
                <div className="app_prev_next_wrapper">
                  <div className="app_prev_next">
                    <div className="app_prev">
                      <GiPreviousButton size={30} />
                    </div>
                    <div className="app_next">
                      <GiNextButton size={30} />
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <Webcam
                audio={false}
                ref={webcamReference}
                screenshotFormat="image/jpeg"
                style={{ width: "100%", maxWidth: "400px" }}
              />
            )}
          </div>
          {/* <div className="app_image">
            {!captured ? (
              <Webcam
                audio={false}
                ref={webcamReference}
                screenshotFormat="image/jpeg"
                style={{ width: "100%", maxWidth: "400px" }}
              />
            ) : (
              <div className="captured_image">
                <div className="captured_inner_image">
                  {selectedImage && (
                    <div className="taken_picture">
                      <img
                        src={selectedImage.image_url}
                        alt="Captured"
                        style={{ maxWidth: "100%" }}
                      />
                    </div>
                  )}
                  {capturedImage && (
                    <div className="taken_picture">
                      <img
                        src={capturedImage}
                        alt="Captured"
                        style={{ maxWidth: "100%" }}
                      />
                    </div>
                  )}
                </div>
                <div className="app_prev_next_wrapper">
                  <div className="app_prev_next">
                    <div className="app_prev">
                      <GiPreviousButton size={30} />
                    </div>
                    <div className="app_next">
                      <GiNextButton size={30} />
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div> */}
          <div className="app_right_icons">
            <div className="app_icon app_right_icon_1">
              <IoPersonAddSharp size={30} />
            </div>
            <div className="app_icon app_right_icon_1">
              <RiDeleteBin5Fill size={30} />
            </div>
            <div className="app_icon app_right_icon_1" onClick={capture}>
              <BsCameraVideoFill size={30} />
            </div>
          </div>
        </div>
        <div className="app_inputChat">
          <textarea
            onChange={handleText}
            placeholder="How may we match your request?"
            name=""
            id=""
            cols="30"
            rows="10"
            className="app_textChat"
          ></textarea>
        </div>
      </div>
    </div>
  );
}

export default App;
