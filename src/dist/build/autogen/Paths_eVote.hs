module Paths_eVote (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch


version :: Version
version = Version {versionBranch = [0,0,0], versionTags = []}
bindir, libdir, datadir, libexecdir :: FilePath

bindir     = "/home/slackwill/.cabal/bin"
libdir     = "/home/slackwill/.cabal/lib/eVote-0.0.0/ghc-7.4.1"
datadir    = "/home/slackwill/.cabal/share/eVote-0.0.0"
libexecdir = "/home/slackwill/.cabal/libexec"

getBinDir, getLibDir, getDataDir, getLibexecDir :: IO FilePath
getBinDir = catchIO (getEnv "eVote_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "eVote_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "eVote_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "eVote_libexecdir") (\_ -> return libexecdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
