import React, { useRef, useCallback, useState } from "react";
import "./App.css";
import { IoColorFilter } from "react-icons/io5";
import { ImBrightnessContrast } from "react-icons/im";
import { TbContrastOff } from "react-icons/tb";
import { IoPersonAddSharp } from "react-icons/io5";
import { RiDeleteBin5Fill } from "react-icons/ri";
import { BsCameraVideoFill } from "react-icons/bs";
import { GiNextButton } from "react-icons/gi";
import { GiPreviousButton } from "react-icons/gi";
import Webcam from "react-webcam";

function App() {
  const [capturedImage, setCapturedImage] = useState(null);
  const [captured, setCaptured] = useState(false);
  console.log(capturedImage);

  const webcamReference = useRef(null);

  const capture = useCallback(() => {
    const imageSrc = webcamReference.current.getScreenshot();
    setCapturedImage(imageSrc);
    setCaptured(true);
  }, [webcamReference]);
  return (
    <div className="app_container">
      <div className="app_wrapper">
        <header className="app_header">
          TEXTILE OPTIONS GENERATING SOFTWARE
        </header>

        <div className="app_image_option_wrapper">
          <div className="app_left_icons">
            <div className="app_icon app_left_icon_1">
              <IoColorFilter size={30} />
            </div>
            <div className="app_icon app_left_icon_1">
              <ImBrightnessContrast size={30} />
            </div>
            <div className="app_icon app_left_icon_1">
              <TbContrastOff size={30} />
            </div>
          </div>
          <div className="app_image">
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
          </div>
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
